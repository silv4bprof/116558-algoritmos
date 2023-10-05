"""
3. Dada uma lista, percorra a mesma multiplicando todos os valores ímpares por 10 e adicione o resultado em uma nova lista chamada 'resultado'.

Lista: 10, 25, 9, 85, 56, 8, 6, 7, 13
Resultado: 250, 90, 850, 70, 130
"""

lista = [10, 25, 9, 85, 56, 8, 6, 7, 13]
resultado = []
for numero in lista:
    if numero % 2 != 0:
        mult = numero * 10
        resultado.append(mult)
print(resultado)
