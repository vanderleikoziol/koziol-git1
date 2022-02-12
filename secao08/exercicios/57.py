import numpy
from numpy.random import default_rng
rng = default_rng(5)
matriz = rng.choice(range(1, 99), size=(7, 6), replace=False)
print(matriz)


def gera_matriz(a, b):
    """
    Recebe uma matriz 7 x 6 e soma a linha informada pelo usuário.

    :param a: matriz 7 x 6 criada pelo rng
    :param b: linha que deve ser somada.
    :return: somatória da linha
    """

    return f'A soma da linha {b} é => {sum(a[b])}'


n = int(input(f'Informe a linha que deve ser somada no intervalo de 0 a 6: '))
print(f'{gera_matriz(matriz, n)}')
