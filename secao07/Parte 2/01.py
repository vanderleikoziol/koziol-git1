print('SOLUÇÃO MODELO 1')
import random

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for x in range(4):
    for y in range(4):
        matriz[x][y] = random.randint(1, 30)
print(f'{"  ".join(map(str, matriz[0]))}\n{"  ".join(map(str, matriz[1]))}\n{"  ".join(map(str, matriz[2]))}'
      f'\n{"  ".join(map(str, matriz[3]))}')
z = len([i for i in (matriz[0] + matriz[1] + matriz[2] + matriz[3]) if i > 10])
print(f'Há {z} números maiores que 10 na matriz.')
print('=-'*30)

print('SOLUÇÃO MODELO 2')
import random
import numpy as np
n = y = 0

matriz = np.zeros([4, 4], int)

for l in range(4):
    for c in range(4):
        matriz[l][c] = random.randint(1, 11)

print(matriz)

for l in range(4):
    for c in range(4):
        if matriz[l][c] > 10:
            n = 1
            y += 1
            print(f'Há {n} número maior que 10 na linha {l+1} coluna {c+1}')
print(f'Há um total de {y} números maiores que 10 na matriz')

