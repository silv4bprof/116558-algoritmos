lista = [1, 2, 3, 4, 5] # tamanho = 5 -> 0 até tamanho - 1
tamanho = len(lista)
print(f'Tamanho da Lista: {tamanho}')

print('Percorrendo normalmente')
for i in range(0, tamanho):
    print(lista[i], end=' ')

print('\n\nPercorrendo de trás pra frente')
contador = 1
for i in range(tamanho):
    posicao = tamanho - contador
    print(f'\nCálculo: tamanho({tamanho}) - contador({contador}) = posicao({posicao})')
    print(f'Posição acessada: {posicao}')
    print(f'Valor da posição {posicao}: {lista[posicao]}')
    contador += 1

'''
1ª Rodada
tamanho = 5
contador = 1
posição = tamanho - contator
posição = 5 - 1 = 4
contador = 1 + 1 = 2

2ª Rodada
tamanho = 5
contador = 2
posição = 5 - 2 = 3
contador = 2 + 1 = 3

3ª Rodada
tamanho = 5
contador = 3
posição = 5 - 3 = 2
contador = 3 + 1 = 4

4ª Rodada
tamanho = 5
contador = 4
posição = 5 - 4 = 1
contador = 4 + 1 = 5

5ª Rodada
tamanho = 5
contador = 5
posição = 5 - 5 = 0

'''