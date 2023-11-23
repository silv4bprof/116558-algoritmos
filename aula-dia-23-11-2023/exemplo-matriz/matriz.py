# listas de listas
# lista = [1, 'Bruno', 3.0, [1,2,4], 5, 6]

matriz = [[1, 2, 3], [4, 5, 6]]
matriz = [
    [1, 2, 3],  # 0
    [4, 5, 6],  # 1
    [7, 8, 9]  # 2
]

# visualizando a matriz
print('\nCru')
print(matriz)

print('\nBonitinha 10x')
for i in range(len(matriz)):
    print(matriz[i])

print('\nLINDA')
for l in range(len(matriz)):  # linhas
    for c in range(len(matriz[l])):  # conta as colunas
        print(matriz[l][c], end=' ')
    print()

# criando a matriz
matriz = []
print('\nMontando uma matriz')
qtd_linhas = int(input('Linhas: '))
qtd_colunas = int(input('Colunas: '))

for l in range(qtd_linhas):
    linha = [0] * qtd_colunas  # [0, 0, 0]
    matriz.append(linha)

print('\nBonitinha 10x')
# print('Coluna:   1  2  3 ... n')
for i in range(len(matriz)):
    print(f"Linha {i}: {matriz[i]}")

# alterando a matriz
print('\nAlterando a matriz:')
pos_linha = int(input('Linha para trocar: '))
pos_coluna = int(input('Coluna para trocar: '))
matriz[pos_linha][pos_coluna] = int(input('Novo Valor: '))

for i in range(len(matriz)):
    print(f"Linha {i}: {matriz[i]}")


print('\nMontando uma NOVA matriz')
matriz = []
qtd_linhas = int(input('Linhas: '))
qtd_colunas = int(input('Colunas: '))

for l in range(qtd_linhas):
    linha = []
    for c in range(qtd_colunas):
        num = int(input(f'Valor da [{l}][{c}]: '))
        linha.append(num)
    matriz.append(linha)

for i in range(len(matriz)):
    print(f"Linha {i}: {matriz[i]}")

print('\nMaior elemento da lista:')
maior = matriz[0][0]
print('Maior elemento inicial:', maior)

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if matriz[l][c] > maior:
            maior = matriz[l][c]

print("Atual maior elemento:", maior)