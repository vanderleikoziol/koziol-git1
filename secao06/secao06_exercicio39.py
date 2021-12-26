"""
Faça um programa que calcule a área de um triangulo, cuja a base e a altura são fornecidas pelo usuário. Esse programa
não pode permitir a entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.

1. O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
2. Chama-se equilátero o triângulo que tem os três lados iguais.
3. Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
4. Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""

import math


# ENTRADA


print('_' * 30)
print('CÁLUCULO DE ÁREA DE TRINANGULOS')
print('_' * 30)


l1 = float(input('Informe a medida do lado A: '))
l2 = float(input('Informe a medida do lado B: '))
l3 = float(input('Informe a medida do lado C: '))


# PROCESSAMENTO


# Área do equilátero


equilatero = (l1 + l2) > l3 and l1 == l2 and l1 == l3
raiz = math.sqrt(3)
altura_equilatero = (l1 * raiz) / 2
area_equilatero = (l1 * altura_equilatero) / 2
perimetro_equilatero = l1 + l2 + l3

# Área do isósceles


isosceles = (l1 + l2) > l3 and l1 == l2 or l1 == l3
l1_base = l2 == l3
l2_base = l1 == l3
l3_base = l1 == l2

if l1_base == True:
    base = (l1 / 2) ** 2
    lado = ((l2 + l3) / 2) ** 2
    valor = lado - base
    raiz = math.sqrt(valor)
    altura_isosceles = raiz
    area_isosceles = (l1 * altura_isosceles) / 2
    perimetro_isosceles = l1 + l2 + l3
elif l2_base == True:
    base = (l2 / 2) ** 2
    lado = ((l1 + l3) / 2) ** 2
    valor = lado - base
    raiz = math.sqrt(valor)
    altura_isosceles = raiz
    area_isosceles = (l2 * altura_isosceles) / 2
    perimetro_isosceles = l1 + l2 + l3
else:
    base = (l3 / 2) ** 2
    lado = ((l1 + l2) / 2) ** 2
    valor = lado - base
    raiz = math.sqrt(valor)
    altura_isosceles = raiz
    area_isosceles = (l3 * altura_isosceles) / 2
    perimetro_isosceles = l1 + l2 + l3
    print('_' * 30)

# Área do escaleno


escaleno = (l1 + l2) > l3 and l1 != l2 and l1 != l3
if escaleno:
    p = (l1 + l2 + l3) / 2

    valor = p * (p - l1) * (p - l2) * (p - l3)

    raiz = math.sqrt(valor)
    area_escaleno = raiz
    perimetro_escaleno = l1 + l2 + l3


# SAÍDA

if equilatero:
        print(f'Os três lados iguais é um triângulo equilátero com:\nAltura => {altura_equilatero:.2f} cm.'
              f'\nPerímetro => {perimetro_equilatero:.2f} cm\nArea => {area_equilatero:.2f} cm².')
elif isosceles:
    print(f'Dois lados iguais é um triângulo isósceles com:\nAltura => {altura_isosceles:.2f} cm\n.'
        f'Perímetro => {perimetro_isosceles:.2f} cm\nÁrea => {area_isosceles:.2f} cm².')
elif escaleno:
    print(
        f'Os três lados diferentes é um triângulo escaleno com:\nSeme perímetro => {p:.2f} cm.\n'
        f'Perímetro => {perimetro_escaleno:.2f} cm\nÁrea => {area_escaleno:.2f} cm².')
else:
    print('Não é um triângulo. A medida do lado precisa ser menor que a soma dos outros dois lados.')
