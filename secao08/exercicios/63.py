def compara_string(a, b):
    """
    Verifica se duas palavras são iguais
    :param a: primeira palavra informada
    :param b: segunda palavra informada
    :return: se as palavras são iguais ou diferentes
    """
    if a == b:
        return 'São iguais'
    return 'São diferentes'


x = input(f'Informe a primeira palavra: ')
y = input(f'Informe a segunda palavra: ')

print(compara_string(x, y))
