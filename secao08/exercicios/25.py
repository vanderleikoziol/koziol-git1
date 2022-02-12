def serie(n):
    s = 0
    for i in range(1, n + 1):
        s += ((i ** 2) + 1) / (i + 3)
    return s


print(serie(int(input(f'Informe um valor: '))))
