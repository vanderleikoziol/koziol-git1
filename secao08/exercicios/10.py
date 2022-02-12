def verifica_maior(*args):
    return max(args)


x = float(input(f'Informe o primeiro número: '))
y = float(input(f'Informe o segundo número: '))


print(f'O maior número é: {verifica_maior(x, y)}')
