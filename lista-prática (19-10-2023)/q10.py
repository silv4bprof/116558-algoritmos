lista = []

while True:
    # A questão pede que seja usando números inteiros ao digitar.
    numero = int(input('Número: '))
    if numero == 0:
        break
    # Porém ao adicionar à lista, eu já converto com string.
    lista.append(str(numero))

numero_unico = ''
# percorro a lista de strings e a cada rodada do for, vou concatenando o valor à variável 'numero_unico'
for elemento in lista:
    numero_unico = numero_unico + elemento

print(numero_unico)
