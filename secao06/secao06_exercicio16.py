"""
Faça um programa que leia um número inteiro positivo impar N e imprima todos os números impares de 1 até N em ordem
decrescente.

"""


num = int(input('Informe um número impar: '))

for n in range(num + 1, 0, -1):
    if n > 0:
        if n % 2 != 0:
            print(n)
    else:
        if num < 0:
            print(f'O número {num} é negativo.')
