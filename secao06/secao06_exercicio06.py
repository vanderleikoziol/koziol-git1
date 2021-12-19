"""
Faça um programa que leia 10 inteiros e imprima sua média.

"""


soma = 0
media = 0
for n in range(1, 10 + 1):
    num = int(input(f'Informe o {n}/10 valor: '))
    soma = soma + num
    media = soma / 10
print(f'A média é: {media}')
