import numpy as np
import random
matrix = np.random.randint(10, size=[3, 3])
x = 0
print(matrix)
for linha in range(3):
    for coluna in range(3):
        if coluna > linha:
            x += matrix[linha][coluna]
print(f'A soma acima da diagonal principal é: {x}')

"""
O for está percorrendo todas as linhas e colunas da matriz.  Sempre que a coluna for maior que a linha a variável x 
será acrescentada com o valor que está na linha e na coluna.
"""