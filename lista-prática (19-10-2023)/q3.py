numeros = []

while True:
    numero = int(input('Número: '))
    if numero == 0: # condição de para escolhida
        break
    else:
        numeros.append(numero)

print(numeros)

print('\nUsando reverse')
numeros.reverse() # o reverse atualiza a minha lista invertendo a ordem dos elementos dentro da mesma variável
print(numeros)
numeros.reverse() # cancelando o reverse para que no próximo bloco a lista serva revertida de outra maneira

print('\nSem usar reverse')
tamanho = len(numeros)
contador = 1
numeros_reverso = []

# essa forma de percorrer funciona da seguinte maneira.
"""
Eu já sei o tamanho da minha lista (tamanho = lento(numeros)).
É criando um contador como inicio em 1, pois com ele eu posso acessar a lista do final pra começo com seguinte fórmula: tamanho - contador, onde o contador vai incrementado a cada rodada, começando sempre em 1 até ele ser igual ao tamanho da lista.

O resultado desse calculo fazer com que a posição acessada seja de trás pra frente.

Ex:

lista = [56, 85, 45, 78]
tamanho = len(lista) # tamanho vai ser 4, sendo a lista seguindo de 0 até 3.
contador = 1 # começa sempre em 1 pra que ao subtrair do tamanho o resultado vai ser exatamente o tamanho da lista, que é 5, subtraído de 1, resultando em 4 (ultimo indice da lista), daí a medida que o contador for aumentando (de um em um ) o 4 vai passar a ser 3, depois 2, depois 1 e por fim 0. Por isso que dentro dos colchetes eu passa a expressão 'tamanho  - contador'.
"""

for i in range(len(numeros)):
    numeros_reverso.append(numeros[tamanho - contador])
    contador += 1

print(numeros_reverso)
