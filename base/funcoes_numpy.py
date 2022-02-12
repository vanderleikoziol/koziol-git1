import random

import numpy
import numpy as np

matriz = np.random.randint(1, 99, size=[4, 4])
print(matriz)

y = np.amax(matriz)
x = numpy.argmax(matriz)
p = np.amin(matriz)
w = numpy.argmin(matriz)
vetor = (np.sum(matriz, axis=0))

print(f'O maior número é {y} e está no indice {x}.')
print(f'O menor número é {p} e está no indice {w}.')
print(f'Array unidimensional das colunas => {vetor}')


