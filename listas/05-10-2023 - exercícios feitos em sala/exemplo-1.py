"""
1. Procurar nome na lista, se achar, exibir o nome a posição dele na lista
"""

# Alternativa 1
nomes = ['bruno', 'josé', 'matheus', 'mariana']
nome = input('Digite um nome: ')
contador = -1
for palavra in nomes:
    contador += 1
    if palavra == nome:
        print(f'Nome {palavra} existe na posição {contador}')

# Alternativa 2
nome = input('Digite um nome: ')
for x in range(0, len(nomes)):
    if nome == nomes[x]:
        print(f'O nome {nome} está na posição {x}')

# Alternativa 3
nome = input('Digite um nome: ')
if nome in nomes:
    posicao = nomes.index(nome)
    print(f'O nome {nome} está na posição {posicao}')