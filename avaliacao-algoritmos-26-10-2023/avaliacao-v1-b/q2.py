alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
palavra = ''
numeros = []

# Percorra o alfabeto e liste as letras com suas posições
print('0: espaço')
for i, letra in enumerate(alfabeto, start=1):
    print(f'{letra}: {i}')

print('\nPreencha a lista com os códigos das letras.')
print('Digite -1 para parar.\n')

while True:
    pos = int(input('Posição da letra no alfabeto: '))
    if pos < 0:
        break
    numeros.append(pos)

for num in numeros:
    if num == 0:
        palavra += ' '
    else:
        palavra = palavra + alfabeto[num - 1]

print('Lista de posições do alfabeto:', numeros)

print('Palavra traduzida:', palavra.upper())
