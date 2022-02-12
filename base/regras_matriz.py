import random
import numpy as np
n = 3
matriz = np.random.randint(1, 10, size=[n, n])
dp = []
ds = []
soma_abaixo_dp = 0
soma_acima_dp = 0
print(f'A matriz é:\n{matriz}')
print('-='*20)
"""
Para calcular a diagonal principal o i (linha) sempre será igual ao j (coluna). Então basta fazer um for para o tamanho
da matriz e um if para a condição i == j.
"""
for i in range(n):
    for j in range(n):
        if i == j:
            dp.append(matriz[i][j])
            print(f'{matriz[i][j]}')

print(f'A diagonal principal é: {dp}')
"""
Para calcular a diagonal secundária o i (linha) sempre será igual ao tamanho da matriz - 1, ou seja, a condição n-1.
Então basta fazer um for para o tamanho da matriz e um if para a i+j = tamanho da matriz -1. 
Observação. Não é possível fazer essa condição com elif se o primeiro if for para calcular a diagonal principal. 
Veja o exemplo para matriz 3 por 3:
 [[1 9 1]
  [3 2 4]
  [4 2 6]]
 O Número 2 está na [linha 1] e na [coluna 1] => essa condição é atendida pela regra da diagonal principal.
 Deste modo se estiver dentro do mesmo if o elif não pega o número da posição que já foi atendidada pelo if. 
"""
print('-='*20)
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            ds.append(matriz[i][j])
            print(f'{matriz[i][j]}')

print(f'A diagonal secundária é: {ds}')

print('-=' * 20)
"""
Abaixo da diagonal principal as linhas sempre serão maiores que as colunas.
"""
for i in range(n):
    for j in range(n):
        if i > j:
            soma_abaixo_dp += (matriz[i][j])
            print(f'{matriz[i][j]}')

print(f'A soma abaixo da diagonal principal é: {soma_abaixo_dp}')

"""
Acima da diagonal principal as colunas sempre serão maiores que as colunas.
"""
for i in range(n):
    for j in range(n):
        if j > i:
            soma_acima_dp += (matriz[i][j])
            print(f'{matriz[i][j]}')

print(f'A soma acima da diagonal principal é: {soma_acima_dp}')


