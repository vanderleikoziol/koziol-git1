"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até n em
ordem crescente.

"""

num = int(input('Informe o número: '))

for n in range(0, num):
    if n >= 0:
        print(n)


