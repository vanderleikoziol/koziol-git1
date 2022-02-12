def eleva_ao_expoente(num1, num2):
    """
    Considera o primeiro número como numerador e o segundo como expoente.
    :param num1: Numerador
    :param num2: Expoente
    :return: resultado do numero 1 elevado ao numero 2
    """
    return num1 ** num2


x = int(input(f'Informe o valor do numerador: '))
z = int(input(f'Informe o valor do expoente: '))

print(eleva_ao_expoente(x, z))
