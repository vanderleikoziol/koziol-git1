"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem
crescente.

"""


num = int(input('Informe um numero: '))

if num > 0:
    for n in range(1, num):
        if n % 2 == 0:
            print(n)
else:
    print(f'O número {num} não é positivo.')
