
import numpy as np
from numpy.random import default_rng
rng = default_rng(5)
a = rng.choice(range(1, 20), size=(4, 4), replace=False)
b = rng.choice(range(1, 20), size=(4, 4), replace=False)


def produto_matriz(x, y):
    """
    Calcula o produto de duas matrizes quadradas.
    :param x: Matriz criada pelo rng
    :param y: Matriz criada pelo rng
    :return: produto das duas matrizes
    """
    c = np.dot(x, y)
    return f'MATRIZ A\n{a}\nMATRIZ B\n{b}\nMATRIZ PRODUTO\n{c}'


print(produto_matriz(a, b))



