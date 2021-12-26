"""
Faça um programa que simula o lançamento de dois dados, d1 e d2, n vezes, e tem como saída o número de cada dado e a
relação entre eles (>,<,=) de cada lançamento.

"""


from random import randint

n = int(input('Informe quantas vezes você quer lançar o dado: '))
print('_' * 20)
for i in range(n):
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    if dado1 > dado2:
        print(f'Dado1 = {dado1}\nDado2 = {dado2}\nDado1 > Dado2')
        print('_' * 20)
    elif dado1 < dado2:
        print(f'Dado1 = {dado1}\nDado2 = {dado2}\nDado1 < Dado2')
        print('_' * 20)
    else:
        print(f'Dado1 = {dado1}\nDado2 = {dado2}\nDado1 = Dado2')
        print('_' * 20)

