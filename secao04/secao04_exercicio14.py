"""
Leia um ângulo em graus (G) e apresente-o convertido em radianos (R).
A fórmula de conversão é:
R = G * π / 180
Sendo π => 3.14

"""

# Enter


g = int(input('Informe quantos graus possui o angulo:  '))

# Processing


r = g * (3.14 / 180)


# Exit


print(f'Um ângulo de {g} graus equivale a {r} radianos')
