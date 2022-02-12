import math


def neperiano(x):
    r = 0
    for i in range(x):
        r += 1 / math.factorial(i)
    return r


n = math.factorial(int(input(f'Informe quantos termos você quer somar: ')))
print(neperiano(n))
