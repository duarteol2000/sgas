from django.urls import path
from . import views

app_name = 'solicitacoes'

urlpatterns = [
    path('cadastrar/', views.cadastrar_solicitacoes, name='cadastrar_solicitacoes'),
    path('cadastrar/<int:id>/', views.cadastrar_solicitacoes, name='editar_solicitacao'), # mudei aqui cadastrar_solicitacoes
    path('confirmacao/<str:protocolo>/', views.confirmacao_solicitacao, name='confirmacao_solicitacao'),
    path('consultar/', views.consultar_protocolo, name='consultar_protocolo'),
]
