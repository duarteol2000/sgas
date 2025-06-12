# core/urls.py
from django.urls import path
from .views import redirecionar_usuario, plataforma, gerar_comprovante_pdf
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('redirecionar/', redirecionar_usuario, name='redirecionar'),
    path('plataforma/', plataforma, name='plataforma'),
    path('exportar-pdf/', views.exportar_pdf, name='exportar_pdf'),  # ← ESSENCIAL
    path('redirecionar/', views.redirecionar_usuario, name='redirecionar_usuario'),
    path('ver_solicitacao/<int:id>/', views.ver_solicitacao, name='ver_solicitacao'),
    path('ver_comprovante/<int:id>/', gerar_comprovante_pdf, name='ver_comprovante'),
]
