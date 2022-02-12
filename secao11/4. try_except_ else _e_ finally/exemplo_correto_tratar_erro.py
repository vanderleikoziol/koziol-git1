"""
Exemplo correto
"""


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possível dividir por zero'


num1 = input(f'Informe o primeiro número: ')
num2 = input(f'Informe o segundo número: ')

print(dividir(num1, num2))
