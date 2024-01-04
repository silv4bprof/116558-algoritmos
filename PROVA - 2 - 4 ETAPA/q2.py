menu = """
Opções:
1. Preencher uma posição qualquer, de escolha do usuário.
2. Exibir a matriz devidamente formatada.
3. Calcular a média de todos os elementos da matriz divisíveis por 3 (se houver).
4. Sair
"""

matriz = []

linhas = int(input('Quantidade de linhas: '))
colunas = int(input('Quantidade de colunas: '))

for l in range(linhas):
    linha = [0] * colunas
    matriz.append(linha)

while True:
    opcao = int(input(f'{menu}\nOpção: '))
    if opcao == 1:
        pos_l = int(input(f'Posição da linha (1 - {linhas}): '))
        pos_c = int(input(f'Posição da coluna (1 - {colunas}): '))
        matriz[pos_l - 1][pos_c - 1] = int(input('Número para inserir: '))
    elif opcao == 2:
        print('\nMatriz Atual')
        for linha in matriz:
            for elemento in linha:
                print(elemento, end=' ')
            print()
    elif opcao == 3:
        soma = 0
        quantidade = 0
        for linha in matriz:
            for numero in linha:
                if numero > 0 and numero % 3 == 0:
                    soma += numero
                    quantidade += 1
        if quantidade > 0:
            print(f'Média dos elementos divisíveis por 3: {soma/quantidade}')
        else:
            print('Sem números divisíveis por 3.')

    elif opcao == 4:
        print('Saindo ...')
        break
    else:
        print('Opção inválida')
