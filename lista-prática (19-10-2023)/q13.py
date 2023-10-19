palavra = input('Palavra: ')

palavra_normal = []
palavra_inversa = []

for elemento in palavra:
    palavra_normal.append(elemento)

for elemento in palavra_normal:
    palavra_inversa.append(elemento)

palavra_inversa.reverse()

print(palavra_normal)
print(palavra_inversa)

if palavra_normal == palavra_inversa:
    print('É palíndromo')
else:
    print('Não é palíndromo')
