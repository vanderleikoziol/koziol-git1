import math

x = int(input(f'Informe o valor do raio da esfera: '))


def volume_esfera(x):
    return 4 / 3 * math.pi * pow(x, 3)


print(f'O volume da esfera é {volume_esfera(x):.2f} m³')



