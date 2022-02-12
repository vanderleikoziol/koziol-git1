import numpy as np

gabarito = ["a", "b", "c", "d", "d", "d", "d", "d", "d", "d"]
array_gabarito = np.zeros([3, 10], str)
array_resposta = np.zeros([3, 10], str)
matricula = []
n = 0
x = 0
while n <= 2:
    matricula.append(int(input(f'Informe a matricula do aluno {n + 1}/3: ')))
    n += 1
for i in range(3):
    for j in range(10):
        array_gabarito[i][j] = gabarito[j]
for i in range(3):
    for j in range(10):
        array_resposta[i][j] = input(
            f'Informe a resposta da matricula n⁰:{matricula[0] + i}, para a questão {j + 1}: ').lower()
acertos = array_resposta.copy()

print('-='*31)
for i in range(3):
    r = 0
    e = 0
    if True:
        for j in range(10):
            if acertos[i][j] == array_gabarito[i][j]:
                r += 1
            else:
                e += 1
    print(f'Gabarito prova => {array_gabarito[i]}')
    print(f'Resposta {matricula[i]}  => {acertos[i]}')
    print(f'Aluno {matricula[i]} => Acertou {r} questões e errou {e} =>', end=' ')
    if r >= 7:
        print(f'Aprovado\n')
    else:
        print(f'Reprovado\n')


print()


