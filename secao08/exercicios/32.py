def func_32(numerador, denominador):
    """
    Encontrar o maior fator possível para divisão do numerador e denominador da fração.
    :param numerador: informado pelo usuário
    :param denominador: informado pelo usuário
    :return: o maior divisor comum para o numerador e denominador
    """
    if numerador <= denominador:
        for i in range(numerador - 1, -1, -1):
            if numerador % i == 0 and denominador % i == 0:
                return i
    else:
        for i in range(denominador - 1, -1, -1):
            if numerador % i == 0 and denominador % i == 0:
                return i


print(func_32(36, 60))
