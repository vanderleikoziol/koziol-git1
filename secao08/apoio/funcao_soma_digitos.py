def soma_digitos(n):
    if n > 0:
        return sum([int(i) for i in list(str(n))])
    return "Valor Inválido"


print(f'A soma dos dígitos é => {soma_digitos(int(input(f"Informe o valor: ")))}')
