"""
Leia quatro notas, calcule a média aritimética e imprima o resultado.

"""

# Entradas


n1 = int(input('Informe a primeira nota: '))
n2 = int(input('Informe a segunda nota: '))
n3 = int(input('Informe a terceira nota: '))
n4 = int(input('Informe a quarta nota: '))

# Processamento


soma = n1 + n2 + n3 + n4
media = soma / 4


# Saída


print(f'A média é {media}.')
