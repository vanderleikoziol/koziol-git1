def caracter():
    """
    Transforma um testo digitado em uma lista. Cada palavra passa a ser um caractere da lista.
    :return: lista
    """
    vetor = input("informe os caracter : ").split(" ")
    return vetor


print(caracter())
