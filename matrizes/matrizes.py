# Matriz 3x3 (nxn)

matriz = []
t_linha = int(input('Linha: '))
t_coluna = int(input('Coluna: '))

# Criando matriz
for i in range(t_linha):
    linha = [0] * t_coluna
    matriz.append(linha)
print(matriz)

# Exibir matriz
for l in range(t_linha):  # Percorre as linhas
    # Percorre as colunas de cada linha (lista) interna
    for c in range(t_coluna):
        print(matriz[l][c], end=" ")
    print()

for l in range(t_linha):
    for c in range(t_coluna):
        matriz[l][c] = int(input(f'Novo valor [{l+1}][{c+1}]: '))

# Exibir matriz
for l in range(t_linha):  # Percorre as linhas
    # Percorre as colunas de cada linha (lista) interna
    for c in range(t_coluna):
        print(matriz[l][c], end=" ")
    print()
