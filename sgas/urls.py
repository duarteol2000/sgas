from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.autenticacao.urls')),
    path('solicitacoes/', include('solicitacoes.urls')),  # <-- adicione isso
]
