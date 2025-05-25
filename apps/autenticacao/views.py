from django.shortcuts import render, redirect
from utils.validacoes import password_is_valid
from autenticacao.models import Usuario
from django.contrib.messages import constants
from django.contrib import messages, auth
from utils.choices import TIPO_USUARIO_CHOICES
from django.contrib.auth.decorators import login_required
from django.urls import reverse



def cadastro(request):
    if request.method == "GET":    
        contexto = {
            "tipo_usuarios": TIPO_USUARIO_CHOICES,
        }
        return render(request, 'autenticacao/cadastro.html', contexto)
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        confirmar_senha = request.POST.get('confirmar_senha')
        nome_completo = request.POST.get('nome_completo')
        tipo = request.POST.get('tipo')
        cep = request.POST.get('cep')
        tipo_logradouro = request.POST.get('tipo_logradouro')
        logradouro = request.POST.get('logradouro')
        numero = request.POST.get('numero')
        cidade = request.POST.get('cidade')
        uf = request.POST.get('uf')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        contato = request.POST.get('contato')
        telefone = request.POST.get('telefone')

        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('autenticacao:cadastro')

        if Usuario.objects.filter(username=username).exists():
            messages.add_message(request, constants.ERROR, "Usuário já cadastrado.")
            return redirect('autenticacao:cadastro')

        if Usuario.objects.filter(email=email).exists():
            messages.add_message(request, constants.ERROR, "E-mail já cadastrado.")
            return redirect('autenticacao:cadastro')
        
        try:

            usuario = Usuario.objects.create_user(
                        username=username,  # herdado de AbstractUser
                        email=email,        # herdado
                        password=senha,     # herdado

                        # Campos personalizados:
                        nome_completo=nome_completo,
                        tipo=tipo,
                        cep=cep,
                        tipo_logradouro=tipo_logradouro,
                        logradouro=logradouro,
                        numero=numero,
                        cidade=cidade,  # um objeto da classe Cidade
                        uf=uf,
                        cpf_cnpj=cpf_cnpj,
                        contato=contato,    # opcional
                        telefone=telefone,
                        is_active=False)
            usuario.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário Cadastrador com Sucesso')
            return redirect(reverse('autenticacao:logar'))
        except Exception as e:
            print('Erro ao cadastrar usuário:', e)
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/auth/cadastro')

        """return HttpResponse('Testando')"""

def logar(request):
    if request.method == "GET":
        return render(request, 'autenticacao/login.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            # Redirecionamento de acordo com o tipo
            if usuario.tipo == 'solicitante':
                return redirect('/solicitacoes/cadastrar/')  # ou use reverse se quiser
            elif usuario.tipo == 'agente':
                return redirect('/painel/agente/')  # ajuste conforme a sua estrutura
            else:
                return redirect('/')  # fallback se o tipo não for reconhecido