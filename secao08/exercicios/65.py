def concatena(a, b, d):
    """
    O usuario informa uma quantidade de letras que deve ser usada da segunda palavra e junta essas letras com a primeira
    palavra.
    :param a: primeira palavra informada pelo usuário
    :param b: segunda palavra informada pelo usuário
    :param d: número de letras informado pelo usuário
    :return: junta parte da segunda palavra com a primeira
    """
    return b[:n] + a


x = input('Digite a primeira string: ')
y = input('Digite a segunda string: ')
n = int(input('Digite a quantidade de caracteres para segunda string: '))

print(concatena(x, y, n))
