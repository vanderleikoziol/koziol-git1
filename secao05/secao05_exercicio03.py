"""
Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário imprima o número ao quadrado.

"""

import math

# Entradas

n = float(input('Informe um número real: '))

# Processamento


if n > 0:
    raiz = math.sqrt(n)
    print(f'A Raiz quadrada de {n} é {raiz:.4f}.')
else:
    q = n ** 2
    print(f'O {n} elevado ao quadrado é {q:.4f}.')
