import random
import numpy as np
n = 3
matriz = np.random.randint(1, 10, size=[n, n])
soma = 0

for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            soma += matriz[i][j]

print(matriz)
print(f'A soma dos elementos da diagonal secundária é: {soma}')
