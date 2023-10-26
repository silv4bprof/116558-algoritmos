# Questões - Fundamentos de Lógica de Algoritmos

<!-- 4 -->
**Questão 01:** Escreva um programa em que o usuário irá fornecer duas listas de inteiros com mesmo tamanho. O tamanho dessas listas também será fornecido pelo usuário ao começar o programa. Os números dessas listas devem ser digitados um a um pelo usuário. Após (SOMENTE APÓS) o programa deverá verificar quais os números são repetidos entre as duas listas e informar esses números ao usuário do programa.

> Atenção: O programa NÃO deve informar ao usuário um número qualquer mais de uma vez.

```python
Digite o tamanho das listas: 4

Digite os números da primeira lista:
Digite o 1º número: 12
Digite o 2º número: 23
Digite o 3º número: 34
Digite o 4º número: 45

Digite os números da segunda lista:
Digite o 1º número: 12
Digite o 2º número: 54
Digite o 3º número: 2
Digite o 4º número: 7

Números repetidos entre as duas listas:
12 
```

**Questão 02:** Escreva um programa em python que, considerando um vetor de caracteres contendo o alfabeto e uma lista de inteiros que vai ser fornecida pelo usuário, encontre uma palavra correspondente aos inteiros. O programa deve considerar que cada inteiro dessa lista, corresponde a posição de uma letra do vetor. Assim, o programa deve percorrer a lista de inteiros e, para cada inteiro, definir a letra correspondente.

> Exemplo: O número 2 corresponde a letra "b". O número 5 corresponde a letra "e".

Como regra para o programa, a palavra deve ser montada após (SOMENTE APÓS) o recebimento dos números fornecidos pelo usuário. O programa deve parar de receber os números quando o usuário digitar um número negativo qualquer.

> Considere que o alfabeto comece com a posição 1 e que o número 0 deva ser um espaço (' ').

```python
# Alfabeto
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Exemplo de funcionamento
Posição da letra no alfabeto: 2
Posição da letra no alfabeto: 18
Posição da letra no alfabeto: 21
Posição da letra no alfabeto: 14
Posição da letra no alfabeto: 15
Posição da letra no alfabeto: -1

Lista de posições do alfabeto: [2, 18, 21, 14, 15]
Palavra traduzida: bruno
```

**Questão 03:** Escreva um programa em python que receba uma palavra fornecida pelo usuário. Após (SOMENTE APÓS) o recebimento da palavra, faça as seguintes operações: 1) Exiba o número de vogais e o número de consoantes da palavra. 2) Crie e exiba uma nova string, trocando cada vogal da palavra por sua versão maiúscula e 3) Preencha e exiba duas novas listas, uma contendo as vogais da string e outra contendo as consoantes.

> Observação: A palavra deve ser informada de uma vez, pelo usuário.

```python
# Exemplos de funcionamento
Palavra: bruno

A palavra bruno contém 2 vogais e 3 consoantes.

Nova string: brUnO

Listas criadas:
Consoantes: ['b', 'r', 'n']
Vogais: ['u', 'o']
```

**Extra (10 pts):** Escreva um programa em python que simule um depósito de produtos, nesse depósito devem ser cadastrados os nome e preço dos produtos. Escreva um programa em python em que o usuário possa guardar os nomes e os preços dos produtos em **UMA LISTA** (use apenas uma lista no programa). Após (SOMENTE APÓS), o programa deve exibir os produtos (nome e preço) adicionados devidamente formatados como mostra o exemplo. Obedecendo à formatação do exemplo.

```python
# Exemplo de funcionamento
CADASTRO DE PRODUTOS

Digite pare no campo de nome para parar.

Nome do produto: Maçã
Valor (R$) do produto: 2.55

Nome do produto: Macarrão
Valor (R$) do produto: 5.99

Nome do produto: pare

# Exemplo de exibição
PRODUTOS CADASTRADOS

Nome: Maçã
Preço: R$ 2.55

Nome: Macarrão
Preço: R$ 5.99
```
