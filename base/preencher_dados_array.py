import random
import numpy as np
matriz = np.zeros([5, 4], int)
x = -1
y = -1
while x <= 4:
    x += 1
    y += 1
    if x <= 4:
        matriz[x][0] = (y + 1000) + 1
        matriz[x][1] = random.randint(1, 5)
        matriz[x][2] = random.randint(1, 5)
        matriz[x][3] = matriz[x][1] + matriz[x][2]
print(matriz)

notas = [matriz[i][3] for i in range(5)]  # criando um vetor da última coluna
matricula_maior_nota = matriz[notas.index(max(notas))][0]  # pegando a linha e a coluna da maior nota
media_notas = round(sum(notas) / 5, 3)  # média entre todas as notas

print(f'\nMatrícula do aluno de maior nota: {matricula_maior_nota}'
      f'\nMédia das notas {media_notas}')
