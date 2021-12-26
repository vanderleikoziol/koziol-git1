"""
Faça um programa que receba um número inteiro maior do que 1, e verifique se o número fornecido é primo ou não.

"""

num = int(input('Informe um número: '))

divisores = []

while num < 1:
    print('Você deve informar um número maior que 1.')
    num = int(input('Informe um número: '))
for i in range(1, num, 1):
    if num % i == 0:
        divisores.append(i)
if len(divisores) == 1 and divisores.__contains__(1) and divisores.__contains__(num):
    print(f'O {num} é um número primo.')
else:
    print(f'O {num} não é um número primo.')



