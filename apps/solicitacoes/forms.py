# solicitacoes/forms.py

from django import forms
from .models import Solicitacao


class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = [
            'especie', 'cep', 'logradouro', 
            'numero', 'complemento',
            'bairro', 'cidade', 'estado',
            'tipo_servico', 'motivo',
            'data_atendimento', 'status',
            'parecer_tecnico', 'resposta_publica',
            'imagem'
        ]
        widgets = {
            'especie': forms.Select(attrs={'class': 'form-control input-form'}),
            'cep': forms.TextInput(attrs={
                'class': 'form-control input-form',
                'placeholder': '00000-000',
                'onblur': 'buscarCep()'
            }),
            'logradouro': forms.TextInput(attrs={'class': 'form-control input-form'}),
            'numero': forms.TextInput(attrs={
                'class': 'form-control input-form',
                'placeholder': 'Ex: 123A'  # Alfanumérico
            }),
            'complemento': forms.TextInput(attrs={'class': 'form-control input-form'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control input-form'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control input-form'}),
            'estado': forms.TextInput(attrs={
                'class': 'form-control input-form', 
                'maxlength': '2',
                'placeholder': 'UF'
            }),
            'tipo_servico': forms.Select(attrs={'class': 'form-control input-form'}),
            'motivo': forms.Textarea(attrs={
                'class': 'form-control input-form',
                'rows': 3,
                'placeholder': 'Descreva o motivo da solicitação'
            }),
            'data_atendimento': forms.DateInput(attrs={
                'class': 'form-control input-form',
                'type': 'date'
            }),
            'status': forms.Select(attrs={'class': 'form-control input-form'}),
            'parecer_tecnico': forms.Textarea(attrs={
                'class': 'form-control input-form',
                'rows': 3,
                'placeholder': 'Parecer técnico da solicitação'
            }),
            'resposta_publica': forms.Textarea(attrs={
                'class': 'form-control input-form',
                'rows': 3,
                'placeholder': 'Texto visível ao solicitante justificando o status atual'
            }),
        }

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.fields['data_atendimento'].required = False
    self.fields['status'].required = False
    self.fields['parecer_tecnico'].required = False
    self.fields['imagem'].required = False
    self.fields['especie'].required = False  # ✅ ESSENCIAL PARA O SOLICITANTE