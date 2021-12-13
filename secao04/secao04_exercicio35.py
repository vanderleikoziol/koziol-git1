"""
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
Hipotenusa = rais quadrada de "a" elevado ao quadrado + "b" elevado ao quadrado.
Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação.
Imprima o resultado desta operação.

"""

# Entradas


a = float(input('Informe o valor do primeiro cateto: '))
b = float(input('Informe o valor do segundo cateto: '))

# Processamento


hipotenusa = ((a ** 2) + (b ** 2)) ** (1/2)


# Saída


print(f'O valor da hipotenusa é {hipotenusa:.2f}')
