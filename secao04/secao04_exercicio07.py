"""
Leia a temperatura em graus Fahrenheit (F) e apresente-a convertida em graus Celsius (C).
A fórmula de conversão é:
C = 5.0 * (F - 32.0) / 9.0
"""
# Enter


f = float(input('Informe a temperatura em graus Fahrenheit: '))


# Processing


c = 5.0 * (f - 32.0) / 9.0

# Exit


print(f'{f} graus Fahrenheit equivale a {c} graus Celsius')
