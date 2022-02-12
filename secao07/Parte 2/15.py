import numpy as np
gabarito = ["a", "b", "c", "d", "d", "d", "d", "d", "d", "d"]
array_gabarito = np.zeros([5, 10], str)
array_resposta = np.zeros([5, 10], str)
resultado = []
a1 = a2 = a3 = a4 = a5 = 0
for i in range(5):
    for j in range(10):
        array_gabarito[i][j] = gabarito[j]
for i in range(5):
    for j in range(10):
        array_resposta[i][j] = input(f'Informe a resposta do aluno {i + 1} para a questão {j + 1}: ').lower()
        if array_resposta[i][j] == array_gabarito[i][j]:
            if i == 0:
                a1 += 1
            elif i == 1:
                a2 += 1
            elif i == 2:
                a3 += 1
            elif i == 3:
                a4 += 1
            elif i == 4:
                a5 += 1
resultado.extend([a1, a2, a3, a4, a5])
print('-='*30)
print(f'O vetor resultados é => {resultado}')
print(f'O aluno 01 acertou {a1} das 10 questões => {(a1/10)*100:.0f}% das questões. ')
print(f'O aluno 02 acertou {a2} das 10 questões => {(a2/10)*100:.0f}% das questões. ')
print(f'O aluno 03 acertou {a3} das 10 questões => {(a3/10)*100:.0f}% das questões. ')
print(f'O aluno 04 acertou {a4} das 10 questões => {(a4/10)*100:.0f}% das questões. ')
print(f'O aluno 05 acertou {a5} das 10 questões => {(a5/10)*100:.0f}% das questões. ')
