# utils/colors.py
from utils.choices import STATUS_CHOICES

CORES_PADRAO = ['bg-warning', 'bg-success', 'bg-primary', 'bg-danger', 'bg-info', 'bg-secondary']

def get_status_colors():
    cores = {}
    for i, (chave, _) in enumerate(STATUS_CHOICES):
        cor = CORES_PADRAO[i % len(CORES_PADRAO)]  # Garante que as cores se repitam se acabar
        cores[chave] = cor
    return cores
