from django.shortcuts import render
from django.shortcuts import render


def arvore_list(request):
    return render(request, 'arvores/listar_arvores.html')
