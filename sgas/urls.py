from django.contrib import admin
from django.urls import path, include
from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # essa linha exibe o index.html na URL /
    path('core/', include('core.urls')),
    path('auth/', include('autenticacao.urls')),
   
]
