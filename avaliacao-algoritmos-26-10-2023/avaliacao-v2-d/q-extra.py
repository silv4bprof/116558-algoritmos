carros = []

print('CADASTRO DE CARROS\n')
print('Digite pare no campo de modelo para parar.')

while True:
    modelo = input('\nModelo: ')
    if modelo == 'pare':
        break
    else:
        placa = input('Placa: ')
        carros.append(modelo)
        carros.append(placa)

print(carros)

print('\nCARROS CADASTRADOS\n')
i = 0
while i < len(carros):
    print(f'Modelo: {carros[i]}\nPlaca: {carros[i+1]}\n')
    i += 2
