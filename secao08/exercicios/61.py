from collections import Counter

x = input("informe uma palavra : ")
y = input("informe a palavra para verificar : ")


def anagrama():
    """
    Verifica se uma palavra é anagrama da outra. Exemplo a palavra pedra e perda.
    :return: True se for anagrama e False se não for
    """
    if len(x) == len(y):
        if Counter(x) == Counter(y):
            return True
    return False


print(anagrama())
