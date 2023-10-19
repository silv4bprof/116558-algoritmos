lista = []
for i in range(1, 21):
    print(i)
    lista.append(i)

# Jeito espeto
print('\nJeito esperto')
print(lista)

# Jeito legal
print('\nJeito legal')
print("[", end='')
tamanho = len(lista)
for i in range(tamanho):
    if i == tamanho - 1:
        print(lista[i], end='')
    else:
        print(lista[i], end=', ')
print("]")
