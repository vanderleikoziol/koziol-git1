info_alunos = ('Matrícula', 'Média_prova', 'Média_trabalho')  # vetor para facilitar na hora do input

matriz = [[int(input(f'{info_alunos[i]}: ')) for i in range(3)] for _ in range(5)]  # preenchendo a matriz

for i in matriz:  # inserindo a coluna das notas finais
    nota_final = (matriz[matriz.index(i)][1] + matriz[matriz.index(i)][2]) / 2  # média das notas de cada aluno
    i.append(nota_final)

for linha in matriz:
    print(linha)

notas = [matriz[i][3] for i in range(5)]  # criando um vetor da última coluna
matricula_maior_nota = matriz[notas.index(max(notas))][0]  # pegando a linha e a coluna da maior nota
media_notas = round(sum(notas) / 5, 3)  # média entre todas as notas

print(f'\nMatrícula do aluno de maior nota: {matricula_maior_nota}'
      f'\nMédia das notas {media_notas}')