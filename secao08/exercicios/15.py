def calcula_triangulo(lado1, lado2, lado3):
    if lado1 < (lado2 + lado3):
        if lado1 == lado2 == lado3:
            return 'Triângulo equilátero'
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return 'Triângulo isósceles'
        elif lado1 != lado2 != lado3:
            return 'Triângulo escaleno'
    return 'Não são medidas de um triângulo!\nO comprimento de cada lado deve ser menor que a soma ' \
           'dos outros dois lados.'


x = int(input(f'Informe o 1⁰ valor: '))
while x <= 0:
    x = int(input(f'\033[0;31mERRO!\33[m=> Informe um valor maior que 0: '))
y = int(input(f'Informe o 2⁰ valor: '))
while y <= 0:
    y = int(input(f'\033[0;31mERRO!\33[m=> Informe um valor maior que 0: '))
z = int(input(f'Informe o 3⁰ valor: '))
while z <= 0:
    z = int(input(f'\033[0;31mERRO!\33[m=> Informe um valor maior que 0: '))

print(calcula_triangulo(x, y, z))
