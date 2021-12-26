"""
Faça um programa que gere um número aleatório de 1 a 100. O usuário deve tentar acertar qual número foi gerado, a cada
tentatively o programa deverá informar se o chute é menor ou maior que o número gerado. O programa acaba quando o
usuário acerta o número gerado. O programa deve informar em quantas tentativas o número foi descoberto.

"""

from random import randint

x = randint(1, 1000)
cont = 0

while True:
    y = int(input('Informe um número: '))
    if y > x:
        cont += 1
        print('Seu chute é maior que o número gerado.')
    elif y < x:
        cont += 1
        print('Seu chute é menor que o número gerado.')
    else:
        break
print(f'Você precisou de {cont} tentativas para acertar o número {x}.')


