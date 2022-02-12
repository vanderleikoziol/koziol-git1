def soma_digitos(n):
    if n > 0:
        return sum([int(i) for i in list(str(n))])
    else:
        return 'Valor inválido'


print(f'A soma dos dígitos é => {soma_digitos(int(input(f"Informe um valor: ")))}')

