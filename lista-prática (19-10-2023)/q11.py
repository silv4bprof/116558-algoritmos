nomes = []

while True:
    nome = input('Nome (pare) para parar: ')
    if nome == 'pare':
        break
    nomes.append(nome)

print('Tamanho:', len(nomes))

print('Primeiro nome:', nomes[0])
print('Ultimo nome:', nomes[len(nomes) - 1])

# A questão pede que seja exibido o nome do meio caso exista
"""
Só existe um meio caso o tamanho da lista seja ímpar
Ex: 
lista1 = ['primeiro', 'meio', 'ultimo'] # elemento do meio é a string 'meio'
lista2 = ['primeiro', 'ultimo'] # não elemento do meio
"""
# se a divisão inteira do tamanho da lista por 2 for 0, quer dizer a lista tem um tamanho par, logo não possui elemento exatamente ao meio
tamanho_lista = len(nomes)
if tamanho_lista % 2 == 0:
    print('Não tem meio')
else:
    # do contrário a lista é de tamanho ímpar, possuindo elemento exatamente ao meio
    meio = ((tamanho_lista + 1) / 2) - 1
    print('índice do elemento exatamente meio:', int(meio))
    print('Nome do meio:', nomes[int(meio)])

"""

Pra acessar o elemento exatamente ao meio, usa-se a fórmula:
( ( tamanho_lista + 1 ) / 2 ) - 1, onde,

tamanho_lista é o len(lista) - 1, pois a lista começa em 0. (vocês já sabem).
O +1 somando ao tamanho da lista é pra deixar o tamanho par e divisão por dois não dar um número quebrado.
Se a lista tem tamanho 5, vai ficar com tamanho 6.
Dividindo por 2, resulta em 3, subtraindo 1, fica 2, que é o indice do elemento exatamente no meio da lista.

lista = ['a', 'b', 'c', 'd', 'e']
indices:  0    1   [2]    3    4

"""