tamanho = int(input("Tamanho das listas: "))

lista1 = []
lista2 = []

# Preenche a primeira lists
print("Digite os números da primeira lista:")
for i in range(tamanho):
    numero = int(input("Digite o {}º número: ".format(i + 1)))
    lista1.append(numero)

print("\nDigite os números da segunda lista:")
for i in range(tamanho):
    numero = int(input("Digite o {}º número: ".format(i + 1)))
    lista2.append(numero)

# Encontra os números repetidos entre as duas listas
numeros_repetidos = []

for numero in lista1:
    if numero in lista2 and numero not in numeros_repetidos:
        numeros_repetidos.append(numero)

# Exibe os números repetidos
if len(numeros_repetidos) > 0:
    print("\nNúmeros repetidos entre as duas listas:")
    for numero in numeros_repetidos:
        print(numero, end=' ')
# Caso não exista nada na lista, exibe uma mensagem
else:
    print("\nNão há números repetidos entre as duas listas.")