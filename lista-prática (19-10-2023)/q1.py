lista = []

while True:
    numero = int(input('Número: '))
    if numero == 0: # condição de para escolhida
        break
    lista.append(numero)

# aqui eu não precisei usar o index() pois como eu já estava percorrendo a lista, eu posso usar o 'i' do for pra me indicar a posição, já que ele representa isso de fato, como podemos ver em 'lista[i]'.
for i in range(len(lista)):
    print(f'Elemento: {lista[i]} - Posição: {i}')
