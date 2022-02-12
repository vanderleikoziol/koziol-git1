import numpy as np
n = 3
x = 0
matriz = np.zeros([n, n], int)
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Informe o valor lina {i+1} Coluna {j+1}: '))
print(matriz)
vetor = (np.sum(matriz, axis=0))
print(f'Array unidimensional => {vetor}')
