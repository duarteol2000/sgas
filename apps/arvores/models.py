from django.db import models
from utils.choices import TAMANHO_CHOICES, TIPO_ARVORE_CHOICES

class EspecieArvore(models.Model):
    nome_popular = models.CharField(max_length=100)
    nome_cientifico = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    tipo = models.CharField(max_length=100, choices=TIPO_ARVORE_CHOICES)
    tamanho = models.CharField(max_length=20, choices=TAMANHO_CHOICES)

    def __str__(self):
        return f"{self.tipo} - {self.nome_popular} - {self.tamanho}"
