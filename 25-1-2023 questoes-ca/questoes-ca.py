# QUESTÃO 1
print('\nQUESTÃO 1')
palavra = 'bruno'
vogais = 'aeiou'

# Exibindo as posições das vogais
print('VOGAIS:')
print(list(palavra)) # ignorar
for i in range(len(palavra)):
    if palavra[i] in vogais:
        print(f'Posição da vogal {palavra[i]}: {i}')

# Exibindo as posições das consoantes
print('\nconsoantes:'.upper())
for i in range(len(palavra)):
    if palavra[i] not in vogais:
        print(f'Posição da consoante {palavra[i]}: {i}')

# QUESTÃO 2
print('\nQUESTÃO 2')
numero = int(input('Número: '))
numero_string = str(numero)
numero_lista = []

# Convertendo em lista
for digito in numero_string:
    numero_lista.append(digito)

print('Número convertido em lista:', numero_lista)

# Convertendo em string novamente
numero_string_novo = ''
for digito in numero_lista:
    numero_string_novo = numero_string_novo + digito

print('\nNúmero convertido em string:', numero_string_novo)
print('\nExibindo na ordem de digitação:')
for dig in numero_string:
    print(dig, end=' ')

print('\n\nExibindo na ordem de digitação (inversa):')
contador = 1
tamanho = len(numero_string)
for i in range(len(numero_string)):
    print(numero_string[tamanho - contador])
    contador += 1

# QUESTÃO 3
print('\nQUESTÃO 3')
palavra = input('Palavra: ')
vogais = 'aeiou'

# Numero de letras da palavra
print('Número de letras:', len(palavra))

# Número de vogais
qtd_vogais = 0
for letra in palavra:
    if letra in vogais:
        qtd_vogais += 1
print('Número de vogais:', qtd_vogais)

# Se sabemos o número de vogais, ao subtrair esse número do total de letras, temos o número de consoantes.
qtd_consoantes = len(palavra) - qtd_vogais
print('Número de consoantes:', qtd_consoantes)
