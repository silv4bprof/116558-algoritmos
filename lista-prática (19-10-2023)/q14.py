lista_1 = []
lista_2 = []
lista_3 = []

print('Lista 1')
for i in range(5):
    nome = input('Nome: ')
    lista_1.append(nome)

print('Lista 2')
for i in range(5):
    nome = input('Nome: ')
    lista_2.append(nome)

# percorrendo listas 1 e 2

for elemento in lista_1:
    if elemento not in lista_3:
        lista_3.append(elemento)

for elemento in lista_2:
    if elemento not in lista_3:
        lista_3.append(elemento)

print('Lista 1:', lista_1)
print('Lista 2:', lista_2)
print('Lista 3:', lista_3)