from numpy.random import default_rng
rng = default_rng()
matriz = rng.choice(range(1, 20), size=(4, 4), replace=False)
print(matriz)
print('-='*8)
for i in range(4):
    for j in range(4):
        if j > i:
            matriz[i][j] = 0
print(f'{matriz}')
