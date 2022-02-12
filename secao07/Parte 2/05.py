import random
import numpy as np
matriz = np.random.randint(1, 25, size=[5, 5])
print(matriz)
n = random.randint(1, 20)
if n in matriz:
    for l in range(5):
        for c in range(5):
            if matriz[l][c] == n:
                print(f'O valor {n} está na linha {l + 1} coluna {c + 1} da matriz.')
else:
    print(f'O valor {n} não foi encontrado na matriz.')
