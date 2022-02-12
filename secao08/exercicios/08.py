import math


def calcula_hipotenusa(cateto1, cateto2):
    return math.sqrt(pow(cateto1, 2) + pow(cateto2, 2))


a = int(input(f'Informe o valor do 1⁰ Cateto: '))
b = int(input(f'Informe o valor do 2⁰ Cateto: '))
print(f'A hipotenusa é: {calcula_hipotenusa(a, b):.2f}')
