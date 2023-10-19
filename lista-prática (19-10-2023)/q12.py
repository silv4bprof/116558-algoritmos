numero = int(input('Número: '))
numero = str(numero)

# Sem usar reverse
tamanho = len(numero)
contador = 1
numeros_reverso = ''

for i in range(len(numero)):
    numeros_reverso += numero[tamanho - contador]
    contador += 1

if numero == numeros_reverso:
    print('É palíndromo')
else:
    print('Não é palíndromo')
