from django.urls import path
from . import views

# apps/agentes/urls.py
app_name = 'agentes'

urlpatterns = [

    path('', views.agentes, name='agentes'),
    path('<int:id>/', views.agentes_list, name='listar_agentes'),

]