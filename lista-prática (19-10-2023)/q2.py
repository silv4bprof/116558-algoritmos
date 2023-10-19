numeros = []

while True:
    numero = int(input('Número: '))
    if numero == 0: # condição de para escolhida
        break
    else:
        numeros.append(numero)

# Já que o for() percorre toda a lista, a partir do primeiro elemento, eu posso usar ele para ir sempre comparando com o elemento seguinte, isso vale para o menor e maior.
maior = numeros[0]
menor = numeros[0]

for i in range(len(numeros)):
    # Caso o número da vez for maior que o numero definido na variavel maior, haverá a troca, fazendo com que a variável maior receba o novo número.
    if numeros[i] > maior:
        maior = numeros[i]

for j in range(len(numeros)):
    # Caso o número da vez for menor que o numero definido na variavel menor, haverá a troca, fazendo com que a variável menor receba o novo número.
    if numeros[j] < menor:
        menor = numeros[j]

print('Maior:', maior)
print('Menor:', menor)