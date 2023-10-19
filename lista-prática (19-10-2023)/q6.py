numeros = []

while True:
    numero = int(input('Número: '))
    if numero == 0:
        break
    numeros.append(numero)

pesquisa = int(input('Número para pesquisa: '))

# Fácil

if pesquisa in numeros:
    print('Numero presente na lista')
else:
    print('Numero não está na lista')

# Legal

existe = False
for i in numeros:
    if pesquisa == i:
        existe = True

if existe:
    print('Numero presente na lista')
else:
    print('Numero não está na lista')
