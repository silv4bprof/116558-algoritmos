l_nome = []
l_sobrenome = []

nome = input('Nome: ')
sobrenome = input('Sobrenome: ')

for i in nome:
    l_nome.append(i)

for i in sobrenome:
    l_sobrenome.append(i)

print(l_nome, 'com', len(l_nome), 'letras')
print(l_sobrenome, 'com', len(l_sobrenome), 'letras')

print('\nSeu nome é:', (l_nome + l_sobrenome))

# Jeito mais legalzinho (percorrendo a lista e criando uma nova string)
nome_completo = ''
for letra in l_nome:
    nome_completo = nome_completo + letra

nome_completo = nome_completo + ' ' # adicionando um espaço antes de passar para percorrer o sobrenome

for letra in l_sobrenome:
    nome_completo = nome_completo + letra

# Jeito mais "pythônico"
l_nome = ''.join(l_nome)
l_sobrenome = ''.join(l_sobrenome)

print('\nSeu nome é:', l_nome, l_sobrenome)