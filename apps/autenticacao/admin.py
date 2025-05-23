from django.contrib import admin

# autenticacao/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {
            'fields': (
                'nome_completo',
                'tipo',
                'cep',
                'tipo_logradouro',
                'logradouro',
                'numero',
                'cidade',
                'uf',
                'cpf_cnpj',
                'contato',
                'telefone',
            )
        }),
    )
