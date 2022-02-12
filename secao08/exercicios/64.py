def concatena_string(str1, str2):
    """
    Soma duas strings informadas
    :param str1: primeira palavra ou testo informado
    :param str2: segunda palavra ou testo informado
    :return:
    """
    return str1 + ' ' + str2


x = input(f'Informe a primeira palavra: ')
y = input(f'Informe a segunda palavra: ')

print(concatena_string(x, y))
