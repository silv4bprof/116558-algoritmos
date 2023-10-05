"""
2. Crie e adicione nomes a uma lista até que seja digitado o numero 0, depois exiba a lista.
"""

nomes = []
while True:
    nome = input('Qual o nome: ')
    if nome == '0':
        break
    else:
        nomes.append(nome)

print(nomes)
