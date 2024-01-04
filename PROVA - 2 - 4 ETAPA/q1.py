matriz = []

while True:
    tam = int(input('Tamanho da matriz: '))
    if tam % 2 != 0:
        break
    print('Tamanho deve ser ímpar, tente novamente!')

for l in range(tam):
    linha = ['_'] * tam
    matriz.append(linha)

print('1º Matriz Inicial')
for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()

print('\n2º Ponto: diagonal principal apenas com 1s.')
for l in range(tam):
    for c in range(tam):
        if l == c:
            matriz[l][c] = 1

for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()

print('\n3º Ponto: demais posições com a letra “A”.')
for l in range(tam):
    for c in range(tam):
        if l != c:
            matriz[l][c] = 'A'

for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()

print('\n4º Ponto: elemento ao meio da matriz, deve ser um “X”')

matriz[tam//2][tam//2] = 'X'

for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
    print()
