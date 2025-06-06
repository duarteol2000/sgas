from django.contrib import admin
from django.urls import path, include
from core.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # essa linha exibe o index.html na URL /
    path('core/', include('core.urls')),
    path('auth/', include('autenticacao.urls')),
    path('localidades/', include('localidades.urls', namespace='localidades')),
    path('agentes/', include('agentes.urls', namespace='agentes')),
    path('solicitantes/', include('solicitantes.urls', namespace='solicitantes')),
    path('solicitacoes/', include('solicitacoes.urls', namespace='solicitacoes')),
    path('arvores/', include('arvores.urls', namespace='arvores')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)