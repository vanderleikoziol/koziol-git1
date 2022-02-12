x = 'Teste de String : '


def retornar():
    """
    Procura uma letra específica dentro de uma palavra.
    :return: a letra se for encontrada e - se não encontrar
    """
    y = input("informe a letra : ")
    if y == 'T':
        print(x[0])
    else:
        print(-1)


retornar()

