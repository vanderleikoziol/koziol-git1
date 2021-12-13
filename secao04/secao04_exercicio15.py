"""
Leia um ângulo em radianos (R) e apresente-o convertido em graus (G).
A fórmula de conversão é:
G = R * 180 / π
Sendo π => 3.14

"""

# Enter


r = float(input('Informe o valor em radianos: '))

# Processing


g = r * (180 / 3.14)

# Exit

print(f'Um ângulo de {r} radianos possui {g} graus')
