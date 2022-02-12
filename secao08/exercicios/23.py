def trinagulo_lateral(n):
    for i in range(1, n + 1):
        print('*' * i)
    for j in range(n - 1, 0, -1):
        print('*' * j)


trinagulo_lateral(int(input(f'Informe o valor: ')))
