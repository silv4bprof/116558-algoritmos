gabarito = []
alunos = []
num_aprovados = 0

qtd_questoes = int(input('Quantidade de questões: '))

print('\nDefinindo o gabarito')
for i in range(qtd_questoes):
    resposta = input(f'Resposta certa (gabarito) para a questão {i+1}: ')
    gabarito.append(resposta)

print('Gabarito:', end=' ')
for r in gabarito:
    print(r, end=' ')

qtd_alunos = int(input('\n\nQuantidade de alunos: '))

for a in range(qtd_alunos):
    aluno = []
    matricula = int(input(f'\nMatrícula do aluno {a+1}: '))
    aluno.append(matricula)
    respostas = []

    for i in range(qtd_questoes):
        resposta = input(
            f'Digite a resposta do aluno {a+1} para a questão {i+1}: ')
        respostas.append(resposta)

    aluno.append(respostas)
    alunos.append(aluno)

for elemento in alunos:
    pontuacao = 0
    print(f'\nResultados do aluno {elemento[0]}')
    print(f'Matrícula: {elemento[0]}')
    print(f'Respostas: {elemento[1]}')
    for i in range(len(elemento[1])):
        if elemento[1][i] == gabarito[i]:
            pontuacao += 1
    print(f'Pontuação: {pontuacao}')

    if pontuacao > 7:
        num_aprovados += 1

print(f'\nNúmero de alunos aprovados: {num_aprovados}')
