from django.db import models


from django.db import models
from autenticacao.models import Usuario

class Solicitante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    email_validado = models.BooleanField(default=False)
    token_validacao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Solicitante: {self.usuario.nome_completo}"
