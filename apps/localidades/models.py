from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    dominio = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
