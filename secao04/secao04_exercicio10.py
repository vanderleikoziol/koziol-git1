"""
Leia uma velocidade em km/h (quilômetros por hora) (K) e apresente-a convertida em m/s (metros por segundo) (M).
A fórmula de conversão é:
M = K / 3.6

"""

# Enter

km_h = int(input('Informe a velocidade em quilômetros por hora: '))

# Processing


mt_s = km_h / 3.6


# Exit


print(f'{km_h} quilômetros por hora é equivalente a {mt_s} metros por segundo.')
