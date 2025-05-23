# solicitacoes/forms.py

from django import forms
from .models import Solicitacao

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = [
            'especie', 'cep', 'tipo_logradouro', 'logradouro',
            'numero', 'complemento', 'bairro', 'estado', 'cidade',
            'motivo', 'status', 'parecer_tecnico', 'imagem'
        ]
