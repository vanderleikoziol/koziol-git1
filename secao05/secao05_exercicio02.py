"""
Leia um número fornecido pelo usuário. Se esse número for positivo calcule a raiz quadrada desse número.
Se o número for negativo mostre a mensagem informando que o número é inválido.

"""

import math

# Entradas


n = int(input('Informe um número: '))

# Processamento


if n > 0:
    raiz = math.sqrt(n)
    print(f'A raiz quadrada do {n} é {raiz:.4f}.')
else:
    print(f'O número informado é inválido!')
