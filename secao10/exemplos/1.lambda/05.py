def geradora_funcao_quadratica(a, b, c):
    """
    Retorna a função f(x) = a*x² + b * x + c
    :param a: informado pelo usuário
    :param b: informado pelo usuário
    :param c: informado pelo usuário
    :return: retorna um lambda
    """
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print('-='*30)

print(geradora_funcao_quadratica(2, 3, -5)(2))

