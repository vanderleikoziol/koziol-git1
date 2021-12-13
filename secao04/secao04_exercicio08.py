"""
Leia a temperatura em graus Kelvin (K) e apresente-a convertida em graus Celsius (C).
A fórmula de conversão é:
C = K - 273.15

"""

# Enter

k = int(input('Informe a temperatura em graus Kelvin: '))

# Processing


c = k - 273.15

# Exit


print(f'{k} graus Kelvin equivale a {c} graus Celsius')
