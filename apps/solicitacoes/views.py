from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime
from apps.solicitacoes.models import Solicitacao, ImagemSolicitacao
from apps.solicitacoes.forms import SolicitacaoForm


@login_required
def cadastrar_solicitacoes(request, id=None):
    usuario = request.user
    tipo_usuario = usuario.tipo

    solicitacao = get_object_or_404(Solicitacao, id=id) if id else None
    imagens = solicitacao.imagens.all() if solicitacao else None

    if request.method == 'POST':
        form = SolicitacaoForm(request.POST, request.FILES, instance=solicitacao)

        if tipo_usuario == 'solicitante':
            form.fields['especie'].required = False
            form.fields['status'].required = False

        if form.is_valid():
            nova_solicitacao = form.save(commit=False)

            if not nova_solicitacao.protocolo:
                agora = datetime.now().strftime('%Y%m%d%H%M%S')
                nova_solicitacao.protocolo = f'SGAS-{request.user.id}-{agora}'

            if not solicitacao:
                nova_solicitacao.solicitante = usuario
                nova_solicitacao.data_solicitacao = timezone.now()

            if tipo_usuario == 'solicitante':
                nova_solicitacao.status = 'pendente'

            nova_solicitacao.save()

            if tipo_usuario != 'solicitante':
                novas_imagens = request.FILES.getlist('imagens')
                imagens_existentes = nova_solicitacao.imagens.count()

                for i, imagem in enumerate(novas_imagens):
                    if imagens_existentes + i >= 4:
                        break
                    ImagemSolicitacao.objects.create(solicitacao=nova_solicitacao, imagem=imagem)

            messages.success(request, f"Sua solicitação foi salva com sucesso. ✅ Protocolo: {nova_solicitacao.protocolo}")
            if tipo_usuario == 'solicitante':
                return redirect('solicitacoes:confirmacao_solicitacao', protocolo=nova_solicitacao.protocolo)
            else:
                return redirect('core:plataforma')
        else:
            messages.error(request, 'Erro ao validar o formulário.')
            print("Erros do formulário:", form.errors)

    else:
        form = SolicitacaoForm(instance=solicitacao)

        if tipo_usuario == 'solicitante':
            form.fields['especie'].required = False
            form.fields['status'].required = False

    contexto = {
        'form': form,
        'solicitacao': solicitacao,
        'tipo_usuario': tipo_usuario,
        'imagens': imagens,
        'data_solicitacao': solicitacao.data_solicitacao if solicitacao else timezone.now().date(),
    }
    return render(request, 'solicitacoes/cadastrar_solicitacoes.html', contexto)


def confirmacao_solicitacao(request, protocolo):
    return render(request, 'solicitacoes/confirmacao.html', {'protocolo': protocolo})


@login_required
def consultar_solicitacao(request):
    protocolo = request.GET.get('protocolo')
    resultado = None
    if protocolo:
        resultado = Solicitacao.objects.filter(protocolo=protocolo).first()
    return render(request, 'solicitacoes/consultar.html', {'resultado': resultado})


def consultar_protocolo(request):
    protocolo = request.GET.get('protocolo')
    resultado = None
    erro = None

    if protocolo:
        try:
            resultado = Solicitacao.objects.get(protocolo=protocolo)
        except Solicitacao.DoesNotExist:
            erro = "Nenhuma solicitação encontrada com este protocolo."

    return render(request, 'solicitacoes/consultar_protocolo.html', {
        'resultado': resultado,
        'erro': erro,
        'protocolo': protocolo
    })
