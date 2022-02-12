def fatorial_quadruplo(n):
    i = n
    n = 1
    while i > 1:
        n *= i
        i -= 4
    return n


print(fatorial_quadruplo(int(input(f'Informe um número: '))))

