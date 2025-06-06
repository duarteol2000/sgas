from django.shortcuts import render
from django.http import HttpResponse
from .models import Solicitante

# Create your views here.
def solicitantes(request):
    return HttpResponse("Página de solicitantes")


# apps/solicitantes/views.py
def solicitante_list(request):
    solicitantes = Solicitante.objects.all()
    return render(request, 'solicitantes/listar_solicitantes.html', {'solicitantes': solicitantes})
