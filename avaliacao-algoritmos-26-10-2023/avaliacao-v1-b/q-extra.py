produtos = []

print('CADASTRO DE PRODUTOS\n')
print('Digite pare no campo de nome para parar.')

while True:
    nome = input('\nNome do produto: ')
    if nome == 'pare':
        break
    else:
        preco = float(input('Valor (R$) do produto: '))    
        produtos.append(nome)
        produtos.append(preco)

print(produtos)

print('\nPRODUTOS CADASTRADOS\n')
i = 0
while i < len(produtos):
    print(f'Nome: {produtos[i]}\nPreço: R$ {produtos[i+1]:,.2f}\n')
    i += 2
