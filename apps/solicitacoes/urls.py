from django.urls import path
from . import views

app_name = 'solicitacoes'

urlpatterns = [
    path('cadastrar/', views.cadastrar_solicitacoes, name='cadastrar'),
]
