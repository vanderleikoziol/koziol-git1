numero = []
altura = []

for i in range(10):
    numero.append(int(input(f'Informe o número do aluno {i + 1}/10: ')))
    altura.append(float(input(f'Informe a altura do aluno{i + 1}/10: ')))

print(f'O aluno mais alto tem {max(altura)}m e o seu código é {numero[altura.index(max(altura))]}.\n'
      f'O aluno mais baixo tem {min(altura)}m e o seu código é {numero[altura.index(min(altura))]}.')
