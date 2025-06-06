# core/urls.py
from django.urls import path
from .views import redirecionar_usuario, plataforma
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('redirecionar/', redirecionar_usuario, name='redirecionar'),
    path('plataforma/', plataforma, name='plataforma'),
]
