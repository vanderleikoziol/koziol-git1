import random
import numpy
import numpy as np
matriz = np.random.randint(1, 99, size=[4, 4])
print(matriz)
n = np.amax(matriz)
y = np.amin(matriz)
x = 0
for l in range(4):
    for c in range(4):
        if matriz[l][c] == n:
            x += 1
            print(f'O maior número é {n} e está na Linha {l + 1} Coluna {c + 1}')
        elif matriz[l][c] == y:
            x += 1
            print(f'O menor número é {y} e está na Linha {l + 1} Coluna {c + 1}')
