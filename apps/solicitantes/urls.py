from django.urls import path
from . import views

# apps/solicitantes/urls.py
app_name = 'solicitantes'


urlpatterns = [
    
    path('solicitantes/', views.solicitantes, name='solicitantes'),
    path('', views.solicitante_list, name='listar_solicitantes'),

]
