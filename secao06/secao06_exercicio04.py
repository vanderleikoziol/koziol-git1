"""
Escreva um programa que declare um inteiro, inicialize com 0, e incremente-o de 1000 em 1000, imprimindo seu valor na
tela, até que seu valor seja 100_000 mil.

"""


n = int(0)

while n < 100_000:
    n = n + 1000
    print(type(n), n)
