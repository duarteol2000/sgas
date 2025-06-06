from django.db import models
from autenticacao.models import Usuario


class AgenteTecnico(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20)
    email_validado = models.BooleanField(default=False)
    token_validacao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Técnico: {self.usuario.nome_completo}"
    
    
class AgenteAdministrativo(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20)
    email_validado = models.BooleanField(default=False)
    token_validacao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Administrativo: {self.usuario.nome_completo}"
