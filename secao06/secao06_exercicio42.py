"""
Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos valores
lidos, o quadrado, o cubo e a raiz quadrada. finalize a entrada de dados com um valor negativo ou zero.

"""


from math import sqrt

while True:
    x = int(input('Informe um valor: '))
    if x > 0:
        q = x ** 2
        c = x ** 3
        r = sqrt(x)
        print(f'O quadrado é: {q}')
        print(f'O cubo é: {c}')
        print(f'A raiz quadrada é: {r:.4f}')
    else:
        break
