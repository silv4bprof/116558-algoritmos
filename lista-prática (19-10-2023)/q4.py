numeros = []

while True:
    numero = int(input('Número: '))
    if numero == 0:
        break
    else:
        numeros.append(numero)

print(numeros)
numeros.sort()
print(numeros)

# ordenação (curiosidade, podem ignorar)
n = len(numeros)

for i in range(n):
    for j in range(0, n-i-1):
        # Percorre a lista a partir do índice 0 até o índice (n - i - 1). A razão pela qual diminuímos i do valor n é que, após cada passagem do algoritmo, o maior elemento na lista já foi colocado em sua posição final.
        if numeros[j] > numeros[j+1]:
            temp = numeros[j]
            numeros[j] = numeros[j+1]
            numeros[j+1] = temp

print(numeros)
