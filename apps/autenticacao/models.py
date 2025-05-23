# autenticacao/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.choices import UF_CHOICES, TIPO_USUARIO_CHOICES


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
    # o campo email e username já vem de AbstractUser

    def __str__(self):
        return f"{self.nome_completo} ({self.email})"
