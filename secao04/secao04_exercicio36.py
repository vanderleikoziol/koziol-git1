"""
Leia a altura (a) e o raio (r) de um cilindro circular em centímetros cúbicos e imprima o volume (V) do cilindro
em metros cúbicos. O volume de um cilindro circular é calculado por meio da seguinte fórmula:
V = π * r² * a
Sendo π => 3.141592

"""

# Entrada


a = float(input('Informe a altura do cilindro: '))
r = float(input('Informe o raio do cilindro: '))

# Processamento


v = (3.141592 * (r ** 2) * a) / 1_000_000

# Saída


print(f'O volume do cilindro é {v:.2f} m³.')
