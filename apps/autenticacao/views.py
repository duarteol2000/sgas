from django.shortcuts import render, redirect
from utils.validacoes import password_is_valid
from django.shortcuts import get_object_or_404
from autenticacao.models import Usuario
from django.contrib.messages import constants
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth import authenticate, login
from utils.choices import TIPO_USUARIO_CHOICES, DOMINIOS_INSTITUCIONAIS
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .utils import gerar_token_confirmacao
from .models import Usuario


def cadastro(request):
    if request.method == "GET":    
        contexto = {
            "tipo_usuarios": TIPO_USUARIO_CHOICES,
            'dominios': DOMINIOS_INSTITUCIONAIS,  # adiciona aqui para usar no template
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
        bairro = request.POST.get('bairro')
        logradouro = request.POST.get('logradouro')
        numero = request.POST.get('numero')
        cidade = request.POST.get('cidade')
        uf = request.POST.get('uf')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        contato = request.POST.get('contato')
        telefone = request.POST.get('telefone')

        if request.method == 'POST':
            print("Dados recebidos:", request.POST)
        
        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('autenticacao:cadastro')

        if Usuario.objects.filter(username=username).exists():
            messages.add_message(request, constants.ERROR, "Usuário já cadastrado.")
            return redirect('autenticacao:cadastro')

        if Usuario.objects.filter(email=email).exists():
            messages.add_message(request, constants.ERROR, "E-mail já cadastrado.")
            return redirect('autenticacao:cadastro')
        
        try:

            usuario = Usuario(
                        username=username,  # herdado de AbstractUser
                        email=email,        # herdado
                        password=senha,     # herdado

                        # Campos personalizados:
                        nome_completo=nome_completo,
                        tipo=tipo,
                        cep=cep,
                        tipo_logradouro=tipo_logradouro,
                        bairro = bairro,
                        logradouro=logradouro,
                        numero=numero,
                        cidade=cidade,  # um objeto da classe Cidade
                        uf=uf,
                        cpf_cnpj=cpf_cnpj,
                        contato=contato,    # opcional
                        telefone=telefone,
                        is_active=False)
            
            # Aqui você gera o token antes de salvar
            usuario.token_confirmacao = gerar_token_confirmacao()

            
            # Define a senha corretamente
            usuario.set_password(senha)   # Validação completa
            usuario.full_clean()          # Roda clean(), validações de campo e choices
            usuario.save()                # Salva no banco

            # Enviar e-mail de confirmação
            link_confirmacao = request.build_absolute_uri(
                reverse('autenticacao:confirmar_email', args=[usuario.token_confirmacao])
            )

            assunto = 'Confirmação de Cadastro - SGAS'
            mensagem = f"Olá {usuario.nome_completo},\n\nPara confirmar seu cadastro, clique no link abaixo:\n\n{link_confirmacao}\n\nObrigado!"

            send_mail(
                assunto,
                mensagem,
                settings.DEFAULT_FROM_EMAIL,
                [usuario.email],
                fail_silently=False,
            )

            messages.add_message(request, constants.SUCCESS, 'Usuário Cadastrador com Sucesso')
            return redirect(reverse('autenticacao:logar'))
        
        except Exception as e:
            print('Erro ao cadastrar usuário:', e)
            messages.add_message(request, constants.ERROR, 'Erro no cadastro: verifique os campos e tente novamente.')
            return redirect('autenticacao:cadastro')

def logar(request):
    if request.method == "GET":
        return render(request, 'autenticacao/login.html')
    
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        usuario = authenticate(username=username, password=senha)

        if not usuario.is_active:
            messages.error(request, 'Sua conta ainda não foi confirmada por e-mail.')
            return redirect('autenticacao:logar')

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('autenticacao:logar')
        
        login(request, usuario)

        #print(f"Usuário autenticado: {usuario}")
        #print(f"Tipo: {getattr(usuario, 'tipo', 'SEM TIPO')}")

        
        
        # ✅ Agora garantimos que o tipo está sendo tratado corretamente
        if hasattr(usuario, 'tipo'):
            if usuario.tipo == 'solicitante':
                return redirect('solicitacoes:cadastrar_solicitacoes')
            else:
                return redirect('core:plataforma')
        else:
            messages.error(request, 'Usuário sem tipo definido.')
            return redirect('index')
        

def confirmar_email(request, token):
    usuario = get_object_or_404(Usuario, token_confirmacao=token)
    usuario.is_active = True
    usuario.token_confirmacao = ''
    usuario.save()
    messages.success(request, 'E-mail confirmado com sucesso! Agora você pode fazer login.')
    return redirect('autenticacao:logar')
        