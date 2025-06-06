from django.http import JsonResponse
from localidades.models import Cidade

def buscar_dominio(request):
    cidade = request.GET.get('cidade', '').strip().lower()
    
    if not cidade:
        return JsonResponse({'erro': 'Cidade obrigatória'}, status=400)

    cidade_obj = Cidade.objects.filter(nome__iexact=cidade).first()
    if not cidade_obj:
        return JsonResponse({'erro': 'Cidade não encontrada'}, status=404)

    return JsonResponse({'dominio': cidade_obj.dominio})