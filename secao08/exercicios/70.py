def reduz(a, b):
    return a / b


def neg(x):
    return -x


def soma(x, y):
    return x + y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))

x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
print()
print('Funcão Reduz: ', reduz(a, b))
print('Funcão neg: ', neg(x))
print('Funcão soma: ', soma(x, y))
print('Funcão mult: ', reduz(x, y))
print('Funcão div: ', div(a, b))