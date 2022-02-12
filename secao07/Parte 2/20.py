from numpy.random import default_rng
rng = default_rng(5)
matriz = rng.choice(range(20), size=(3, 6), replace=False)
vetor_impar = []
vetor_2_4_coluna = []
print(matriz)

for i in range(3):
    for j in range(6):
        if j % 2 != 0:
            vetor_impar.append(matriz[i][j])
for i in range(3):
    for j in range(6):
        if j == 1 or j == 3:
            vetor_2_4_coluna.append(matriz[i][j])

print(f'O vetor impar é: {vetor_impar}')
print(f'O vetor impar é: {vetor_2_4_coluna}')
print(f'A soma das colunas impares é: {sum(vetor_impar)}')
print(f'A media dos elementos da segunda e quarta coluna é: {sum(vetor_2_4_coluna) / len(vetor_2_4_coluna):.2f}')


print(matriz[2:3])
