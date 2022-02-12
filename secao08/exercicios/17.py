def soma_inteiros(num1, num2):
    """
    Soma números no intervalo dos parâmetros.
    :param num1: primeiro número digitado
    :param num2: segundo número digitado
    :return: somatória dos números existentes no intervalo
    """
    matriz = []
    cont = 0
    if num1 < num2:
        a = num2 - num1
        for n in range(a):
            cont += 1
            matriz.append(num1 + cont)
        return sum(matriz)
    else:
        a = num1 - num2
        for n in range(a):
            cont += 1
            matriz.append(num2 + cont)
        return sum(matriz)


x = int(input(f'Informe o 1⁰ Número: '))
y = int(input(f'Informe o 2⁰ Número: '))

print(soma_inteiros(x, y))
