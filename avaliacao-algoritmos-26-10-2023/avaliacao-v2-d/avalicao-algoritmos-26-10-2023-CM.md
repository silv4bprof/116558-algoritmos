# Questões - Fundamentos de Lógica de Algoritmos

<!-- 5 -->
**Questão 01:** Escreva um programa em que o usuário irá fornecer duas listas de inteiros com mesmo tamanho. O tamanho dessas listas também será fornecido pelo usuário ao começar o programa. Os números dessas listas devem ser digitados um a um pelo usuário. Após (SOMENTE APÓS) o programa deve verificar quais os números das duas lista NÃO são repetidos entre as duas listas e informar ao usuário.

> Atenção: O programa NÃO deve informar ao usuário um número qualquer mais de uma vez.

```python
Digite o tamanho das listas: 4

Digite os números da primeira lista:
Digite o 1º número: 1
Digite o 2º número: 45
Digite o 3º número: 3
Digite o 4º número: 5

Digite os números da segunda lista:
Digite o 1º número: 5
Digite o 2º número: 1
Digite o 3º número: 34
Digite o 4º número: 5

Números que não se repetem entre as duas listas:
45 3 34 
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

**Questão 03:** Escreva um programa em python que preencha uma lista com letras, o usuário deve escolher quantas letras deverão ser inseridas na lista. Após (SOMENTE APÓS) o preenchimento, faça as seguintes operações: 1) Exiba o número de vogais e o número de consoantes da lista. 2) Crie e exiba uma nova lista, trocando cada vogal da lista por sua versão maiúscula e 3) Preencha e exiba duas novas listas, uma contendo as vogais da string e outra contendo as consoantes.

> Observação: O usuário deve digitar letra por letra no programa para que o programa possa acrescentar todas as letras no vetor e executar sua missão.

```python
# Exemplos de funcionamento
Quantidade de letras: 6

Letra: d
Letra: a
Letra: n
Letra: i
Letra: e
Letra: l

Palavra:  ['d', 'a', 'n', 'i', 'e', 'l']

A palavra ['d', 'a', 'n', 'i', 'e', 'l'] contém 3 vogais e 3 consoantes.

Nova string: dAnIEl

Listas criadas:
Consoantes: ['d', 'n', 'l']
Vogais: ['a', 'i', 'e']
```

**Extra (10 pts):** Escreva um programa em python que simule um depósito de carros, nesse depósito devem ser cadastrados os modelo e a placa dos carros. Escreva um programa em python em que o usuário possa guardar os modelos e as placas dos carros em **UMA LISTA** (use apenas uma lista no programa). Após (SOMENTE APÓS), o programa deve exibir os carros (modelo e placa) adicionados devidamente formatados como mostra o exemplo. Obedecendo à formatação do exemplo.

```python
# Exemplo de funcionamento
CADASTRO DE CARROS

Digite pare no campo de modelo para parar.

Modelo: uno
Placa: 123-yuio

Modelo: Fox
Placa: 890-hjks

Modelo: pare

# Exemplo de exibição
CARROS CADASTRADOS

Modelo: uno
Placa: 123-yuio

Modelo: Fox
Placa: 123-hjks
```
