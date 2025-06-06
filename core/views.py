# apps/core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.solicitacoes.models import Solicitacao
from utils.choices import STATUS_CHOICES
from utils.color import get_status_colors
from datetime import datetime


def index(request):
    return render(request, 'core/index.html')


@login_required
def redirecionar_usuario(request):
    user = request.user
    if user.tipo == 'solicitante':
        return redirect('solicitacoes:cadastrar_solicitacoes')
    elif user.tipo == 'tecnico':
        return redirect('core:plataforma')  # Corrigido: prefixo 'core'
    else:
        return redirect('logout')


@login_required
def plataforma(request):
    ano_atual = datetime.now().year
    solicitacoes_ano = Solicitacao.objects.filter(data_solicitacao__year=ano_atual)

    # Contador por status (pendente, concluído, cancelado)
    contagem_status = {
        chave: solicitacoes_ano.filter(status=chave).count()
        for chave, _ in STATUS_CHOICES
    }

    # Cores dos cards por status
    cores_status = get_status_colors()  # ← ✅ Gera dicionário de cores dinâmico


    # Lista geral de solicitações
    solicitacoes = Solicitacao.objects.all()

    contexto = {
        'contagem_status': contagem_status,
        'cores_status': cores_status,  # ← Passa para o template
        'solicitacoes': solicitacoes,
        'status_choices': STATUS_CHOICES,
    }

    return render(request, 'core/plataforma.html', contexto)
