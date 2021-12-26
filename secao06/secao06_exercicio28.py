"""
Faça um programa que leia o valor N inteiro e positivo, calcule e mostre o valor E, conforme fórmula a seguir:
E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!

"""

from math import factorial

numero = 1
soma = 0
print('Digite zero para sair')

while numero > 0:
    numero = int(input('Informe um número: '))
    for i in range(1, numero + 1):
        soma += 1 / factorial(i)
    print(f'A soma da serie de {numero} é {soma:.4f}.')
