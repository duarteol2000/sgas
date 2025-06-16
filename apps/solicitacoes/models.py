from django.db import models
from arvores.models import EspecieArvore
from autenticacao.models import Usuario
from utils.choices import TIPO_SERVICO, STATUS_CHOICES

class Solicitacao(models.Model):
    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitacoes')
    protocolo = models.CharField(max_length=30, unique=True, blank=True, null=True)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    data_atendimento = models.DateTimeField(blank=True, null=True)
    especie = models.ForeignKey(EspecieArvore, on_delete=models.SET_NULL, null=True, blank=True)
    cep = models.CharField(max_length=10)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=25)
    estado = models.CharField(max_length=2)
    tipo_servico = models.CharField(max_length=10, choices=TIPO_SERVICO)
    motivo = models.TextField()
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    parecer_tecnico = models.TextField(blank=True, null=True)
    resposta_publica = models.TextField("Resposta para o Solicitante", blank=True, null=True)
    imagem = models.ImageField(upload_to='solicitacoes/', blank=True, null=True)

    def __str__(self):
        return f"{self.solicitante.nome_completo} - {self.logradouro}, {self.numero} - {self.status}"
    
class ImagemSolicitacao(models.Model):
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='solicitacoes/imagens/')
    descricao = models.CharField(max_length=255, blank=True)
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagem da Solicitação #{self.solicitacao.id} - {self.solicitacao.solicitante.nome_completo}"

