"""
Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.

"""


cont = 0
soma = 0
media = 0
for n in range(1, 10 + 1):
    num = int(input(f'Informe o número {n}/10 valor: '))
    if num > 0:
        cont = cont + 1
        soma = soma + num
        media = soma / cont
    else:
        cont = cont
        media = media
print(f'A média é: {media}')
