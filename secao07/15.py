import numpy as np
matriz = np.zeros([5, 10], str)
gabarito = []
n = 0
y = 0
for k in range(ord('a'), ord('d') + 1):
    gabarito.append(chr(k))
while n <= 9:
    for i in range(10):
        for j in range(4):
    n += 1
    y += 1
    matriz[0][0] = input(f'Informe a resposta do aluno {y} para a pergunta {n}: ')
print(matriz)
print(gabarito)
