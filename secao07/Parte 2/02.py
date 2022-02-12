import numpy as np
print('SOLUÇÃO MODELO 1')

matriz = np.zeros([5, 5], int)
lc = 0
while lc <= 4:
    matriz[lc, lc] = 1
    lc += 1
print(matriz)

print('=-'*35)

print('SOLUÇÃO MODELO 2')

matriz = [[], [], [], [], []]
y = 0

while y <= 16:
    for x in range(0, 5):
        matriz[x].insert(1, 0)
        y += 1
for z in range(0, 5):
    matriz[z].insert(z, 1)
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}\n{matriz[3]}\n{matriz[4]}', end='')
print()
