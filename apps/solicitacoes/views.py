from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SolicitacaoForm

def cadastrar_solicitacoes(request):
    if not request.user.is_authenticated:
        return redirect('autenticacao:login')

    solicitante = request.user

    if request.method == 'POST':
        form = SolicitacaoForm(request.POST, request.FILES)
        if form.is_valid():
            solicitacao = form.save(commit=False)
            solicitacao.solicitante = solicitante
            solicitacao.save()
            messages.success(request, "Solicitação cadastrada com sucesso!")
            return redirect('pagina_inicial')
        else:
            messages.error(request, "Erro ao cadastrar solicitação. Verifique os dados.")
    else:
        form = SolicitacaoForm()

    return render(request, 'solicitacoes/cadastro_solicitacoes.html', {
        'form': form,
        'solicitante': solicitante
    })
