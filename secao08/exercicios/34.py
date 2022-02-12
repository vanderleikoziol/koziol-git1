def fatorial_duplo(n):
    i = n
    n = 1
    while i > 1:
        n *= i
        i -= 2
    return n



print(fatorial_duplo(int(input(f'Informe um número: '))))