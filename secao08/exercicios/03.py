x = int(input(f'Informe um valor: '))


def verifica(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


print(verifica(x))
