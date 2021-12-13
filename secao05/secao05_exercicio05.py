"""
Faça um programa que receba um número inteiro e verifique se esse número é par ou impar.

"""

# Entradas


n = int(input('Informe o número: '))

# Processamento


if n % 2 > 0:
    print(f'O número {n} é impar.')
else:
    print(f'O número {n} é par.')
