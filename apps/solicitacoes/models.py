from django.db import models
from arvores.models import EspecieArvore
from autenticacao.models import Usuario


STATUS_CHOICES = [
    ('pendente', 'Pendente'),
    ('em_analise', 'Em Análise'),
    ('atendido', 'Atendido'),
    ('indeferida', 'Indeferida'),
]

class Solicitacao(models.Model):
    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    especie = models.ForeignKey(EspecieArvore, on_delete=models.PROTECT)
    cep = models.CharField(max_length=10)
    tipo_logradouro = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=25)
    estado = models.CharField(max_length=2)
    motivo = models.TextField()
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    parecer_tecnico = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='solicitacoes/', blank=True, null=True)

    def __str__(self):
        return f"{self.solicitante.nome_completo} - {self.logradouro}, {self.numero} - {self.status}"
