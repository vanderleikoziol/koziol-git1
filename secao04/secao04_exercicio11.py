"""
Leia uma velocidade em em m/s (metros por segundo) (M) e apresente-a convertida km/h (quilômetros por hora) (K).
A fórmula de conversão é:
K = K * 3.6
"""

# Enter


metros = int(input('Informe o valor em metros: '))

# Processing


k = metros * 3.6

# Exit


print(f'{metros} por segundo equivale a {k} quilômetros por hora.')
