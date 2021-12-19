"""
Faça um programa que some todos os numeros naturais abaixo de 1000 que são multiplos de 3 e 5.

"""

soma = 0

for divisor in range(1, 1000):
    if divisor % 3 == 0 or divisor % 5 == 0:
        soma = soma + divisor
        print(divisor)
print(f'A soma dos multiplos de 3 e 5 é {soma}.')
