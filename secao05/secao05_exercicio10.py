"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes
fórmulas (onde h corresponde a altura):

Homens (72.7 * h) - 58
Mulheres (62.1 * h) - 44.7

"""

sexo = input('Informe seu sexo (M ou F): ')
h = float(input('Informe sua altura: '))


if sexo.lower() == 'm':
    peso_ideal = (72.7 * h) - 58
    print(f'Seu peso ideal é {peso_ideal:.2f}.')
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * h) - 44.7
    print(f'Seu peso ideal é {peso_ideal:.2f}.')
