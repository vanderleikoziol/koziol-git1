"""
Escreva um programa que leia um número inteiro maior do que zero e devolva na tela a soma de todos seus algarismos.
Por exemplo, o número 251 corresponderá ao valor 8(2 + 5 + 1). S o nú,ero lido não for maior de que zero, o programa
terminará com a mensagem 'Número Inválido'

"""

n = input('Informe um número maior que zero e de três dígitos: ')

if n > str(0):
    print(f' Soma = {int(n[0]) + int(n[1]) + int(n[2])}')
else:
    print('Número inválido.')
