# utils/choices.py

# Choices para 'UF' (Estados)
UF_CHOICES = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
    ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'),
]


# Choices para 'Tipo de Usuário'
TIPO_USUARIO_CHOICES = [
    ('solicitante', 'Solicitante'),
    ('administrativo', 'Administrativo'),
    ('tecnico', 'Técnico'),
]

# Choices para 'Tamanho da Árvore'
TAMANHO_CHOICES = [
    ('pequeno', 'Pequeno'),
    ('medio', 'Médio'),
    ('grande', 'Grande'),
]

# Choices para 'Tipo de Árvore' (Exemplo fictício, adicione conforme necessário)
TIPO_ARVORE_CHOICES = [
    ('frutifera', 'Frutífera'),
    ('ornamental', 'Ornamental'),
    ('nativa', 'Nativa'),
    ('exotica', 'Exótica'),
]

DOMINIOS_INSTITUCIONAIS = {
    'Maracanaú': '@maracanau.ce.gov.br',
    'Fortaleza': '@fortaleza.ce.gov.br',
    'Caucaia': '@caucaia.ce.gov.br',
    'Pacatuba': '@pacatuba.ce.gov.br',
    'Aquiraz': '@aquiraz.ce.gov.br',
    'Eusébio': '@eusebio.ce.gov.br',
    'Itaitinga': '@itaitinga.ce.gov.br',
    'Guaiúba': '@guaiuba.ce.gov.br',
}


TIPO_SERVICO = {
    'Poda': 'Poda',
    'Corte': 'Corte',
    'Plantio': 'Plantio',
}

#    ('em_analise', 'Em Análise'),
STATUS_CHOICES = [
    ('pendente', 'Pendente'),
    ('atendido', 'Atendido'),
    ('indeferido', 'Indeferido'),
]