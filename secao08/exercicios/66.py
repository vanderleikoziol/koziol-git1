def retorna_maiusculo(a):
    """
    Retorna caractere em maiúsculo.
    :param a: caracter informado pelo usuário
    :return: caractere em maiúsculo
    """
    return a.upper()


y = input(f'Informe uma letra: ')
print(retorna_maiusculo(y))
