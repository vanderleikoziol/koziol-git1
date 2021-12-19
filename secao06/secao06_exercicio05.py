"""
Faça um programa que peça ao usuário para digitar 10 valores e some-os.

"""

soma = 0
for n in range(1, 10 + 1):
    num = int(input(f' Informe o número {n}/10 valor: '))
    soma = soma + num
print(f' A soma é: {soma}')
