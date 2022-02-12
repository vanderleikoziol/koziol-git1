def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'


num1 = input(f'Informe o primeiro número: ')
num2 = input(f'Informe o segundo número: ')

print(dividir(num1, num2))

print('-='*30)


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError, TypeError)as err:
        return f'Ocorreu um problema: {err}'


num1 = input(f'Informe o primeiro número: ')
num2 = input(f'Informe o segundo número: ')

print(dividir(num1, num2))
