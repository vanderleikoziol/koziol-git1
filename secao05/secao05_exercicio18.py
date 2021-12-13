"""
Faça um programa que mostre ao usuário um menu com quatro opções de operações matemáticas (as básicas, por exemplo)
O usuário pede uma das opções e seu programa então pede dois valores numéricos e realiza a operação, mostrando o
resultado e saindo.

"""


print('OPERAÇÕES MATEMÁTICAS')
print('_' * 20)
print('Para soma digite 1:')
print('Para subtrair digite 2:')
print('Para multiplicar digite 3:')
print('Para dividir digite 4:')

operacao = int(input('Informe qual tipo de operação você deseja realizar: '))


if operacao == 1:
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))
    r = n1 + n2
    print(f'O resultado de {n1} + {n2} é : {r}')
elif operacao == 2:
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))
    r = n1 - n2
    print(f'O resultado de {n1} + {n2} é : {r}')
elif operacao == 3:
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))
    r = n1 * n2
    print(f'O resultado de {n1} * {n2} é : {r}')
elif operacao == 4:
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))
    r = n1 / n2
    print(f'O resultado de {n1} / {n2} é : {r}')
else:
    print('Opreação não identificada')









