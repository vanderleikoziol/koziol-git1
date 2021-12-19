"""
Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais impares.

"""
cont = 0
numero = int(input('Informe o número: '))

for n in range(numero):
    if n % 2 != 0:
        print(n)
