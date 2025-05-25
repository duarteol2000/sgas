from django.urls import path
from . import views

app_name = 'autenticacao'

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='logar'),
    
]
