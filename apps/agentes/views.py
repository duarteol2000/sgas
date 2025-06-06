from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def agentes(request):
    return HttpResponse("Página de agentes")

def agentes_list(request, id):
    return HttpResponse(f"Lista de agentes com ID: {id}")

