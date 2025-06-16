from django.urls import path
from . import views

app_name = 'autenticacao'

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='logar'),  
    path('confirmar_email/<str:token>/', views.confirmar_email, name='confirmar_email'),
]
