# solicitacoes/admin.py

from django.contrib import admin
from .models import Solicitacao

@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'solicitante',
        'especie',
        'logradouro',
        'numero',
        'bairro',
        'cidade',
        'status',
        'data_solicitacao',
    )
    list_filter = ('status', 'cidade', 'bairro', 'especie')
    search_fields = ('solicitante__nome_completo', 'logradouro', 'bairro', 'cidade')
    readonly_fields = ('data_solicitacao',)
