def soma26s8(n):
    lista = []
    cont = 0
    for i in range(1, n + 1):
        cont += 1
        lista.append(cont)
    print(f'A soma é => {sum(lista)}')


soma26s8(int(input(f'Informe um valor: ')))
