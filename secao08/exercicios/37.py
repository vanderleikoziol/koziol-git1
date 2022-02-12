import math


def hiperfatorial(n):
    soma = 1
    for i in range(1, n + 1):
        x = pow(math.factorial(i), i)
        soma = soma * x
    return soma


print(hiperfatorial(int(input(f'Informe o valor: '))))