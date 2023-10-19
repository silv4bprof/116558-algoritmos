notas = []

for i in range(4):
    nota = int(input('nota: '))
    notas.append(nota)

# Já que o for() percorre toda a lista, a partir do primeiro elemento, eu posso usar ele para ir sempre comparando com o elemento seguinte, isso vale para o menor e maior.
maior = notas[0]
menor = notas[0]

for i in range(len(notas)):
    if notas[i] > maior:
        maior = notas[i]

for j in range(len(notas)):
    if notas[j] < menor:
        menor = notas[j]

soma = 0
for c in range(len(notas)):
    soma = soma + notas[c]

print('Maior:', maior)
print('Menor:', menor)
print('Média:', (soma/len(notas)))
