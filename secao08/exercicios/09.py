import math


def volume_cilindro(altura, raio):
    return math.pi * pow(raio, 2) * altura


x = float(input(f'Informe a altura do cilindro em metros: '))
y = float(input(f'Informe o raio do cilindro em metros: '))

print(f'O volume do cilindro é {volume_cilindro(x, y):.2f} m³')
