import random
import numpy as np
x = 4
n = 0
matriz_a = np.random.randint(1, 99, size=[x, x])
matriz_b = np.random.randint(1, 99, size=[x, x])
matriz_c = np.zeros([x, x], int)
print(f'{matriz_a}')
print('-='*7)
print(f'{matriz_b}')
print('-='*7)
while n <= x * x:
    for l in range(x):
        for c in range(x):
            if matriz_a[l][c] > matriz_b[l][c]:
                matriz_c[l][c] = matriz_a[l][c]
            else:
                matriz_c[l][c] = matriz_b[l][c]
            n += 1
print(matriz_c)





