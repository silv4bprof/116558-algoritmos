numero = int(input('Numero: '))
if numero > 1000:
    numero_str = str(numero)

    tamanho = len(numero)
    contador = 1
    numeros_reverso = ''

    for i in range(len(numero)):
        numeros_reverso += numero[tamanho - contador]
        contador += 1

    print(numeros_reverso)
else:
    print('Número precisa ser maior que 1000')