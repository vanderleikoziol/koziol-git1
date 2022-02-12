def operacao(num1, num2, s):
    if s == '+':
        return num1 + num2
    elif s == '-':
        return num1 - num2
    elif s == '/':
        return num1 / num2
    elif s == 'x':
        return num1 * num2
    else:
        return '\033[0;31mESCOLHA INVÁLIDA.\33[m'


tipo = 0
v1 = int(input(f'Informe 1⁰ valor: '))
v2 = int(input(f'Informe 2⁰ valor: '))
x = input(f'Informe o tipo de operação desejada:\n1. Para soma informe => +\n2. Para subtrair informe => -\n'
          f'3. Para dividir informe => /\n4. Para multiplicar informe => x\nEscolha sua opção: ').lower()
if x == '+':
    tipo = 'soma'
elif x == '-':
    tipo = 'subtração'
elif x == '/':
    tipo = 'divisão'
elif x == 'x':
    tipo = 'multiplicação'

print(operacao(v1, v2, x))


