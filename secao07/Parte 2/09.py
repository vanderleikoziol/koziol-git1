import numpy as np
import random
matriz = np.random.randint(1, 10, size=[3, 3])
x = 0
for linha in range(3):
    for coluna in range(3):
        if coluna < linha:
            x += matriz[linha][coluna]
print(f'{matriz}\nA soma dos elementos que estão abaixo da diagonal principal é: {x}.')
