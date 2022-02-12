def triangulo(n):
    cont = 1
    for i in reversed(range(1, n + 1)):
        x = ' ' * i
        y = '*' * cont
        cont += 2
        print(x + y)

    for j in range(n):
        print(f'{" " * n }**')




triangulo(int(input(f'Informe um valor: ')))
