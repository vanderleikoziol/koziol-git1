"""
Tpo Booleano
Algebra Booleana, criada por George Boole.
Há dua constantes: o Verdadeiro ou Falso
True or False => sempre com as iniciais maiúsculas.
"""
ativo = False
print(ativo)
"""
Operações básicas
Negação (note):
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso e se for falso o resultado será verdadeiro.
Ou seja, sempre ao contrário.
Veja neste caso onde ativo = False, se eu executar print(not ativo) True

not True = False
not False = True
"""
print(not ativo)
logado = False

"""
Or => operação binária que depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True => True
True ou False => True
False or True = True
False or False => False
"""
print(ativo or logado)
#note que neste caso ativo => False e logado => Falso então o resultado é False se executar.

"""
Operação com and
Também é uma operação binária que depende de dois valore. Ambos os valores devem ser verdadeiros
True and True => True
True and False => False
False and True = False
False and False => False

5 > 6 => False
5 < 6 => True
6 == 6 => True
4 <= 5 => True
Podemos fazer o mesmo com variáveis
num1 = 7
num2 = 8
num1 >= num2 => False
num1 == num2 => False

num1 < num2 or num1 > 3 => True
num1 < num2 and num1 > 3 => True
"""

5 > 6
type(True)

