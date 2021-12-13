"""
Faça um programa que leia o valor de um produto e imprima o valor com desconto.
 Valor do desconto => 12%.

"""

# Entradas


valor = int(input('Informe o valor do produto: '))

# Processamento


valor_com_desconto = valor - (valor * (12 / 100))


# Saída


print(f'O valor com desconto é {valor_com_desconto:.2f}')
