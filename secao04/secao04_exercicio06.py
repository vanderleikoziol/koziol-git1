"""
Leia a temperatura em graus Celsius (C) e apresente-a convertida em graus Fahrenheit (F).
A fórmula de conversão é:
F = C * (9.0 / 5.0) + 32
"""
# Enter


c = int(input('Informe a temperatura em graus Celsius: '))

# Processing

f = c * (9.0 / 5.0) + 32.0


# Exit


print(f'{c} graus Celsius é equivalente a {f} graus Fahrenheit')
