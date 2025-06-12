from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse
from apps.solicitacoes.models import Solicitacao
from utils.choices import STATUS_CHOICES
from utils.color import get_status_colors
from django.template.loader import get_template
from django.templatetags.static import static
from django.conf import settings
from reportlab.pdfgen import canvas
from io import BytesIO
from xhtml2pdf import pisa
import os


def index(request):
    return render(request, 'core/index.html')


@login_required
def redirecionar_usuario(request):
    user = request.user
    if user.tipo == 'solicitante':
        return redirect('solicitacoes:cadastrar_solicitacoes')
    elif user.tipo == 'tecnico':
        return redirect('core:plataforma')
    else:
        return redirect('logout')


@login_required
def plataforma(request):
    ano_atual = datetime.now().year
    solicitacoes_ano = Solicitacao.objects.filter(data_solicitacao__year=ano_atual)

    contagem_status = {
        chave: solicitacoes_ano.filter(status=chave).count()
        for chave, _ in STATUS_CHOICES
    }

    cores_status = get_status_colors()

    campo = request.GET.get('campo')
    valor = request.GET.get('valor', '').strip()
    solicitacoes = Solicitacao.objects.all()

    if not campo or not valor:
        solicitacoes = solicitacoes.filter(status='PENDENTE')
    else:
        if campo == 'nome':
            solicitacoes = solicitacoes.filter(solicitante__nome_completo__icontains=valor)
        elif campo == 'cpf':
            valor_limpo = valor.replace('.', '').replace('-', '')
            solicitacoes = solicitacoes.filter(solicitante__cpf_cnpj__icontains=valor_limpo)
        elif campo == 'protocolo':
            solicitacoes = solicitacoes.filter(protocolo__icontains=valor)
        elif campo == 'status':
            solicitacoes = solicitacoes.filter(status=valor.upper())
        elif campo == 'data':
            try:
                from django.db.models.functions import TruncDate
                data_formatada = datetime.strptime(valor, '%Y-%m-%d').date()
                solicitacoes = solicitacoes.annotate(data_pura=TruncDate('data_solicitacao')).filter(data_pura=data_formatada)
            except ValueError:
                solicitacoes = Solicitacao.objects.none()

    contexto = {
        'contagem_status': contagem_status,
        'cores_status': cores_status,
        'solicitacoes': solicitacoes,
        'status_choices': STATUS_CHOICES,
    }

    return render(request, 'core/plataforma.html', contexto)



@login_required
def exportar_pdf(request):
    # Mesmos filtros da view plataforma()
    status = request.GET.get('status')
    nome = request.GET.get('nome')
    cpf = request.GET.get('cpf')
    protocolo = request.GET.get('protocolo')
    data = request.GET.get('data')

    solicitacoes = Solicitacao.objects.all()

    if not status:
        solicitacoes = solicitacoes.filter(status='PENDENTE')
    else:
        solicitacoes = solicitacoes.filter(status=status.upper())

    if nome:
        solicitacoes = solicitacoes.filter(solicitante__nome__icontains=nome)
    if cpf:
        solicitacoes = solicitacoes.filter(solicitante__cpf__icontains=cpf)
    if protocolo:
        solicitacoes = solicitacoes.filter(protocolo__icontains=protocolo)
    if data:
        try:
            data_formatada = datetime.strptime(data, '%Y-%m-%d').date()
            solicitacoes = solicitacoes.filter(data_solicitacao=data_formatada)
        except ValueError:
            pass

    # Geração do PDF
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setTitle("Solicitações - SGAS")

    pdf.drawString(100, 800, "Relatório de Solicitações (filtro aplicado)")
    y = 780

    for s in solicitacoes:
        linha = f"ID: {s.id} | Solicitante: {s.solicitante.nome_completo} | Status: {s.get_status_display()} | Data: {s.data_solicitacao.strftime('%d/%m/%Y')}"
        pdf.drawString(50, y, linha)
        y -= 20
        if y < 50:
            pdf.showPage()
            y = 800

    pdf.save()
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=\"relatorio_solicitacoes.pdf\"'
    return response


def ver_solicitacao(request, id):
    solicitacao = get_object_or_404(Solicitacao, id=id)
    return render(request, 'core/ver_solicitacao.html', {'solicitacao': solicitacao})


@login_required
def gerar_comprovante_pdf(request, id):
    solicitacao = Solicitacao.objects.select_related('solicitante').get(id=id)

    # Caminhos absolutos das imagens
    logo_meio_ambiente = os.path.join(settings.BASE_DIR, 'static', 'solicitacoes', 'img', 'logo_meio_ambiente.png')
    logo_renea = os.path.join(settings.BASE_DIR, 'static', 'solicitacoes', 'img', 'logo_renea.png')  # substitua pelo correto

    contexto = {
        'solicitacao': solicitacao,
        'logo_meio_ambiente': logo_meio_ambiente,
        'logo_renea': logo_renea,
    }

    template_path = 'solicitacoes/comprovante_pdf.html'
    template = get_template(template_path)
    html = template.render(contexto)

    buffer = BytesIO()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="comprovante_{solicitacao.protocolo}.pdf"'

    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), buffer)
    if not pdf.err:
        response.write(buffer.getvalue())
        return response
    else:
        return HttpResponse("Erro ao gerar PDF", status=500)
