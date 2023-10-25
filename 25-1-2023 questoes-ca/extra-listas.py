import os

# Percorrendo listas
lista = []
tamanho = 20

# Preenchendo listas com números naturais
for i in range(1, tamanho + 1):
    lista.append(i)

for x in lista:
    print(x, end=' ')

print()

for index, value in enumerate(lista):
    print(f'Índice: {index} - Valor: {value}')

print('\nFatiamento')
for x in lista[10:15]:
    print(x, end=' ')
print()

for index, value in enumerate(lista[10:15]):
    print(f'Índice: {lista.index(value)} - Valor: {value}')

print('\nPercorrendo de trás pra frente')
for x in lista[::-1]:
    print(x, end=' ')

print('\nou')

for x in reversed(lista):
    print(x, end=' ')

print()
lista.sort()
print(lista)

os.system('cls')

print('\nListas'.upper())

print('\nLista desordenada (formato inicial):')
lista = [22, 333, 2, 23, 23, 2, 43, 4, 23, 45, 35, 34, 5, 34, 534]
print(lista)

print('\nLista reversa:')
lista.reverse()
print(lista)

print('\nLista ordenada:')
lista.sort()
print(lista)

print('\nLista ordenada (invertida):')
lista.sort()
lista.reverse()
print('USANDO: sort() & reverse():', lista)

# ou

lista = [22, 333, 2, 23, 23, 2, 43, 4, 23, 45, 35, 34, 5, 34, 534]
lista.sort(reverse=True)
print('USANDO: sort(reverse=True):', lista)

print('\nStrings'.upper())

lista = list('111')
print(lista)