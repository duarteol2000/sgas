from django.urls import path
from . import views

app_name = 'localidades'

urlpatterns = [
    path('buscar-dominio/', views.buscar_dominio, name='buscar_dominio'),
]
