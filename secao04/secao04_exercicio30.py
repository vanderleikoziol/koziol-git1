"""
Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólar.

"""

# Entradas

real = float(input('Informe o valor em R$: '))
cotacao_dolar = float(input('Informe a cotação do dólar: '))

# Processamento

dolar = real / cotacao_dolar

# Saída


print(f'{real} reais equivalem a {dolar:.4f} dólar.')
