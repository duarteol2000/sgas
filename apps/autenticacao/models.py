# autenticacao/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from utils.choices import UF_CHOICES, TIPO_USUARIO_CHOICES, DOMINIOS_INSTITUCIONAIS


class Usuario(AbstractUser):
    nome_completo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)
    cep = models.CharField(max_length=9)
    tipo_logradouro = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=25)
    bairro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    uf = models.CharField(max_length=2, choices=UF_CHOICES)
    cpf_cnpj = models.CharField(max_length=18)
    contato = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20)
    token_confirmacao = models.CharField(max_length=64, blank=True, null=True)
    # o campo email e username já vem de AbstractUser

    def clean(self):
        """
        Valida se o e-mail institucional está correto para usuários do tipo administrativo ou técnico.
        """
        if self.tipo in ['administrativo', 'tecnico']:
            cidade_formatada = self.cidade.strip().title()

            dominio_esperado = DOMINIOS_INSTITUCIONAIS.get(cidade_formatada)

            if not dominio_esperado:
                raise ValidationError({'cidade': f"A cidade '{self.cidade}' não possui domínio institucional configurado."})

            if not self.email.endswith(dominio_esperado):
                raise ValidationError({
                    'email': f"E-mail institucional inválido. Deve terminar com '{dominio_esperado}'."
                })
            
    def __str__(self):
        return f"{self.nome_completo} ({self.email})"
