tamanho = int(input("Digite o tamanho das listas: "))

lista1 = []
lista2 = []

# Preenche as listas
print("\nDigite os números da primeira lista:")
for i in range(tamanho):
    numero = int(input("Digite o {}º número: ".format(i + 1)))
    lista1.append(numero)

print("\nDigite os números da segunda lista:")
for i in range(tamanho):
    numero = int(input("Digite o {}º número: ".format(i + 1)))
    lista2.append(numero)

# Encontra os números que não se repetem entre as duas listas
numeros_nao_repetidos = []

for numero in lista1:
    if numero not in lista2 and numero not in numeros_nao_repetidos:
        numeros_nao_repetidos.append(numero)

for numero in lista2:
    if numero not in lista1 and numero not in numeros_nao_repetidos:
        numeros_nao_repetidos.append(numero)

# Exibe os números que não se repetem
if len(numeros_nao_repetidos) > 0:
    print("Números que não se repetem entre as duas listas:")
    for numero in numeros_nao_repetidos:
        print(numero, end=' ')
# Caso não exista nada na lista, exibe uma mensagem
else:
    print("Não há números que não se repetem entre as duas listas.")