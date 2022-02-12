import random

n = ['a', 'b', 'c', 'd']
matriz_gabarito = [random.sample(n, 1) for gabarito in range(10)]
print(f'Gabarito => {matriz_gabarito}')

matriz_resposta = [[random.sample(n, 1) for resposta in range(10)] for valor in range(3)]
for i in range(3):
    print(f'Aluno{i+1} => ', end='')
    for j in range(10):
        print(f'{matriz_resposta[i][j]}', end='')
