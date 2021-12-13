"""
Calcule as raízes da equação de segundo grau.

E ax² + bx + c = 0 => representação da equação de segundo grau.
A variável a deve ser diferente de zero. Caso seja igual, imprima a mensagem 'Não é uma equação do segundo grau'.

1. Se Δ < 0 => Não existe real. Imprima a mensagem não existe raiz.
2. Se Δ = 0 => Existe uma raíz real. Imprima a raíz e a mensagem raíz única.
3. Se Δ > 0 => Imprima as duas raízes reais.
"""

import math


print('Calcule as raízes da equação de segundo grau. \nE ax² + bx + c = 0 => representação da equação de segundo grau.'
      ' \nA variável a deve ser diferente de zero. \nCaso seja igual, imprima a mensagem: Não é uma equação do segundo '
      'grau.\n1. Se Δ < 0 => Não existe real. Imprima a mensagem não existe raiz.\n2. Se Δ = 0 => Existe uma raíz real.'
      ' Imprima a raź e a mensagem raíz única. \n3. Se Δ > 0 => Imprima as duas raízes reais.')

print('_' * 80)

a = float(input('Informe o coeficiente da variável a = '))
b = float(input('Informe o coeficiente da variável b = '))
c = float(input('Informe o coeficiente da variável c = '))

if a == 0:
    print('Não é uma equação do segundo grau')
else:
    delta = b ** 2 - 4 * a * c
    print(f'o valor de delta é: {delta}.')
    if delta < 0:
        print('Não existe raíz.')
    elif delta == 0:
        raiz = math.sqrt(delta)
        print(f'A raiz de delta é: {raiz}.')
        x2linha = ((-b + raiz) / (2 * a)) * (- 1)
        print(f'O valor da raíz única é: {x2linha}.')
    else:
        raiz = math.sqrt(delta)
        print(f'A raiz de delta é: {raiz}.')
        xlinha = ((-b - raiz) / (2 * a)) * (- 1)
        print(f"O valor de x' é: {xlinha}.")
        x2linha = ((-b + raiz) / (2 * a)) * (- 1)
        print(f'O valor de x" é: {x2linha}.')



