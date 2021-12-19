"""
Faça um programa que um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente.

"""

num = int(input('Informe o número: '))

if num > 0:
    for n in range(num, 0, -1):
        if n % 2 == 0:
            print(n)
else:
    print(f'O número {num} não é positivo.')
