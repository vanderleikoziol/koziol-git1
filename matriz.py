import numpy as np

matriz = np.zeros([10, 10], int)

print(matriz)

for i in range(10):
    for j in range(10):
        if i < j:
            matriz[i][j] = int(2 * i + 7 * j - 2)
        elif i == j:
            matriz[i][j] = int(3 * (i ** 2) - 1)
        elif i > j:
            matriz[i][j] = int((4 * (i ** 3)) - (5 * (j ** 2)) + 1)
print(matriz)

