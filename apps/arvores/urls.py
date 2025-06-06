from django.urls import path
from . import views

app_name = 'arvores'

urlpatterns = [
    path('', views.arvore_list, name='listar_arvores'),  # ou qualquer nome que esteja usando
]
