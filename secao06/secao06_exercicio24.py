"""
Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com excessão dele
próprio. Ex. A soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

"""

soma = 0
n = int(input('Informe um número: '))

for divisor in range(1, n, 1):
    if n % divisor == 0:
        soma = soma + divisor
        print(divisor)
print(f'A soma dos divisores é: {soma}.')

