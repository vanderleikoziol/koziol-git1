"""
Faça um programa que calcule e mostre a area de um trapézio. Sabe-se que:

       (B + b) * h
A  =   ___________
           2

"""


def area(base_maior, base_menor, altura):
    a = (base_maior + base_menor) * altura / 2
    print(f'A área do trapézio é de: {a:.2f} metros quadrados ')


print(' Área de trapézio')
print('_' * 20)
b2 = float(input('Informe a medida da base maior: '))
b1 = float(input('Informe a medida da base menor: '))
h = float(input('Informe a medida da altura: '))
area(b2, b1, h)
