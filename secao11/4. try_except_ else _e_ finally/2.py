"""
Exemplo errado
"""



def dividir(a, b):
    return a / b


num1 = int(input(f'Informe o primeiro número: '))
try:
    num2 = int(input(f'Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico')
try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

