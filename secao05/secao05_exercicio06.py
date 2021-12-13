"""
Escreva um programa que, dado dois números inteiros, mostre na tela o maior deles, assim como a diferença existente
entre eles.

"""

# Entrada


n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

# Processamento


if n1 > n2:
    d = n1 - n2
    print(f'O maior número é {n1} e a diferença entre {n1} e {n2} é {d}.')
else:
    d = n2 - n1
    print(f'O maior número é {n2} e a diferença entre {n1} e {n2} é {d}.')

