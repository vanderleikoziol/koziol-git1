import math


def superfatorial(n):
    soma = 1
    for i in range(1, n + 1):
        x = math.factorial(i)
        soma = soma * x
    return soma


print(superfatorial(int(input(f'Informe o valor: '))))
