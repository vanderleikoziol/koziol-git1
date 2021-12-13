"""
Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a
mensagem números iguais.

"""

# Entradas


n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

# Processamento


if n1 > n2:
    print(n1)
elif n1 == n2:
    print(f'Os números são iguais.')
else:
    print(n2)
