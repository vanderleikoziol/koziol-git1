import numpy
import numpy as np
from numpy.random import default_rng
rng = default_rng(3)
matriz = rng.choice(range(10), size=(10, 3), replace=True)
print(matriz)
n = numpy.amin(matriz)
for i in range(3):
    x = 0
    if True:
        for j in range(10):
            if matriz[j][i] == n:
                x += 1
    print(f'A menor nota da prova {i+1} é {n} e o número de alunos que tirou {n} é: {x}')
