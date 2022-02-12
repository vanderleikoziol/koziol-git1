import random
import numpy as np
n = 3
matriz = np.random.randint(1, 10, size=[n, n])
x = 0
for linha in range(n):
    x += matriz[linha][linha]
    print(f'{linha} => {matriz[linha][linha]}')

print(f'{matriz}\nA soma da diagonal é: {x}.')

"""
O segredo aqui está em informar apenas a linha.
O range está indo até três e neste caso estou informando apenas a linha. Então na primeira passada está pegando o
elemento do indice 0 da linha 0, na segunda passada está pegando o elemento 1 da posição 1 da linha 1 e na terceira 
passada pega o elemento 2 da posição 2 da linha 2.
"""