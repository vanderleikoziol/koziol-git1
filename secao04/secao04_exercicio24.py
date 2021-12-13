"""
Leia um valor de área em metros quadrados m² (M) e apresente-o convertido em acres (A).
A fórmula de conversão é:
A = M * 0.000247

"""

# Entrada


m = float(input('Informe a área em m²: '))


# Processamento


a = m * 0.000247


# Saída


print(f'{m} m² equivalem a {a} acres.')
