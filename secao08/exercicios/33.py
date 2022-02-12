def s833(n):
    if n > 0:
        return sum([int(i) for i in list(str(n))])
    return 'Valor inválido'


print(s833(int(input(f'Informe um valor: '))))

