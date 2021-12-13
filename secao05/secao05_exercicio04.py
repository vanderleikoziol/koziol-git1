"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre.
a) O número digitado ao quadrado.
b) A raiz quadrada do número digitado.

"""
import math

# Entradas


n = int(input('Informe um número: '))

# Processamento


if n > 0:
    quadrado = n ** 2
    raiz = math.sqrt(n)
    print(f'O número {n} elevado ao quadrado é {quadrado}.')
    print(f'A Raiz quadrada do numero {n} é {raiz:.0f}.')
