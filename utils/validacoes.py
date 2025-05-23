import re
from django.contrib import messages
from django.contrib.messages import constants


def cpf_cnpj_is_valid(request, cpf_cnpj):
    if len(cpf_cnpj) < 8 or len(cpf_cnpj) > 14:
        messages.add_message(request, messages.ERROR, 'Seu CPF ou CNPJ está com número incorreto')
        return False
    return True
    

def password_is_valid(request, password, confirm_password):
    if len(password) < 6:
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter 6 ou mais caractertes')
        return False

    if not password == confirm_password:
        messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
        return False
    
    if not re.search('[A-Z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas')
        return False

    if not re.search('[a-z]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minúsculas')
        return False

    if not re.search('[1-9]', password):
        messages.add_message(request, constants.ERROR, 'Sua senha não contém números')
        return False

    return True