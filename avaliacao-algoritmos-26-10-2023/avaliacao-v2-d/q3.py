vogais = 'aeiou'
qtd_vogais = 0
qtd_consoantes = 0
palavra = []

qtd_letras = int(input('Quantidade de letras: '))
print()

for i in range(qtd_letras):
    letra = input('Letra: ')
    palavra.append(letra)

print('\nPalavra: ', palavra)
    
nova_string = ''

for letra in palavra:
    if letra in vogais:
        qtd_vogais += 1

qtd_consoantes = len(palavra) - qtd_vogais

print(
    f'\nA palavra {palavra} contém {qtd_vogais} vogais e {qtd_consoantes} consoantes.')

# nova string
for letra in palavra:
    if letra in vogais:
        nova_string += letra.upper()
    else:
        nova_string += letra

print(f'\nNova string: {nova_string}')
consoantes_palavra = []
vogais_palavra = []

for letra in palavra:
    if letra in vogais:
        vogais_palavra.append(letra)
    else:
        consoantes_palavra.append(letra)

print('\nListas criadas:')
print('Consoantes:', consoantes_palavra)
print('Vogais:', vogais_palavra)
