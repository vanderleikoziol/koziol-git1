"""
Tipo numérico

1. Se eu usar // retorna um numero inteiro de uma divisão
 1 / 2 -> 2.5
 1 // 2 -> 2

2. Se eu quiser saber o resto da divisão eu utilizo o módulo:
  4 % 2 -> 0 (quatro módulo de 2 é zero, ou seja, não tem resto.
  7 % 2 -> 1
  5 % 2 -> 1
  Observações: toda vez que eu fizer modulo de 2 para um número impar o resultado será zero.

3. Para elevar um númeero a uma potência eu utilizo:

2 ** 2 => 4
Não há limite de tamanho de um número inteiro em Python.

4. Para facilitar a leitura de um número pode ser utilizado o _.

1_000_000 => Um milhão. Assim fica mais fácil a leitura do que 1000000.
Eu posso declarar uma variável num = 42
ptint(num)
42
num + 1
43
print(num + 1)
43
num += 1 => isso é o mesmo que num = num + 1 => (número recebe número mais 1)
num
43
num -= 1 => isso é o mesmo que num = num - 1 => (número recebe número menos 1)

num *= 2 => 86 (número recebe número vezes dois)
num /= 2 => 86 (número recebe número dividido por dois)
Para eu saber qual o tipo de variável eu posso utilizar:
exemplo:
num = 42
type(num)
Retorna => 'int'

Eu também poderia perguntar:
type(23)
Retorna
'int'

Neste caso eu já tenho uma variável declarada onde num = 42
então
num
retorna
42
dir(nun) => vai retornar todas as operações que posso fazer com essa variável
Veje, já sei que o num = 42
então se eu usar:
num.__add__(8) => 50 (ou seja, foi acrescentado 8 ao 42)
"""

num = 1_000_000
print(num)
print(float(num))

