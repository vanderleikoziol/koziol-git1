"""
Faça um programa que leia um número inteiro positivo impar N e imprima todos os números impares de 1 até N em ordem
crescente.

"""


num = int(input('Informe um número impar: '))

for n in range(0, num + 1):
    if n > 0:
        if n % 2 != 0:
            print(n)
    else:
        if num < 0:
            print(f'O número {num} não é positivo.')
    