from django.shortcuts import render, redirect
from django import template

register = template.Library()

@register.filter
def get_item(dicionario, chave):
    return dicionario.get(chave, 'bg-secondary')  # Retorna a cor cinza se a chave não existir)@
