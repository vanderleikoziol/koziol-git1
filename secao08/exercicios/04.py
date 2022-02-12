from math import sqrt

x = int(input(f'Informe um número: '))


def quadrado_perfeito(x):
    if sqrt(x) / int(sqrt(x)) == 1:
        return f'O número {x} é um quadrado perfeito e sua raiz quadrada é o => {sqrt(x):.0f}'
    return f'O número {x} não é um quadrado perfeito!'


print(quadrado_perfeito(x))
