"""
Leia a nota e o número de faltas de um aluno, escreva seu conceito de acordo com a tabela abaixo. Quando o aluno tem
mais de 20 falatas ocorre uma redução de conceito.

   NOTA              CONCEITO ATÉ 20 FALTAS     CONCEITO MAIS DE 20 FALATAS
9.0 até 10.0                    A                             B
7.5 até 8.9                     B                             C
5.0 até 7.4                     C                             D
4.0 até 4.9                     D                             E
0.0 até 3.9                     E                             E

"""

x = float(input('Informe a nota: '))
y = float(input('Informe o número de faltas: '))

if 0.0 <= x <= 3.9:
    if y <= 20:
        conceito = 'E'
        print(f'Seu conceito é: {conceito}')
    else:
        conceito = 'E'
        print(f'Seu conceito é: {conceito}')
elif 4.0 <= x <= 4.9:
    if y <= 20:
        conceito = 'D'
        print(f'Seu conceito é: {conceito}')
    else:
        conceito = 'E'
        print(f'Seu conceito é: {conceito}')
elif 5.0 <= x <= 7.4:
    if y <= 20:
        conceito = 'C'
        print(f'Seu conceito é: {conceito}')
    else:
        conceito = 'D'
        print(f'Seu conceito é: {conceito}')
elif 7.5 <= x <= 8.9:
    if y <= 20:
        conceito = 'B'
        print(f'Seu conceito é: {conceito}')
    else:
        conceito = 'C'
        print(f'Seu conceito é: {conceito}')
elif 9.0 <= x <= 10.0:
    if y <= 20:
        conceito = 'A'
        print(f'Seu conceito é: {conceito}')
    else:
        conceito = 'B'
        print(f'Seu conceito é: {conceito}')
else:
    print('Nota fora do parâmetro.\nInforme uma nota de 0 a 10.')



