print('\n\Lista de caracteres para string:')
nome_l = ['b', 'r', 'u', 'n', 'o']
print(nome_l)

nome_s = ''
print('\nAntes:', nome_s)
for letra in nome_l:
    print('Durante:', nome_s)
    print(f'{nome_s} + {letra} = {nome_s + letra}')
    nome_s = nome_s + letra  # a + b = ab
print('\nDepois:', nome_s)

# string para lista de caracteres
print('\n\nString para lista de caracteres:')
lista_c = []
print(nome_s)
for letra in nome_s:
    lista_c.append(letra)
print(lista_c)

print('\n\nNúmeros para string')
numero_l = [1, 2, 3]
numero_i = 678

numero_l_s = []
for i in range(len(numero_l)):
    aux = str(numero_l[i])
    numero_l_s.append(aux)
print(numero_l_s)

numero_string = ''
for i in numero_l_s:
    numero_string += i
print(numero_string)