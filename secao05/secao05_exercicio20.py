"""
Dados três valores A, B e C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, se é um
triângulo escaleno, equilátero ou isóscele,considerando os seguintes conceitos:

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

# Área do escaleno


escaleno = (l1 + l2) > l3 and l1 != l2 and l1 != l3
if escaleno:
    p = (l1 + l2 + l3) / 2
    print(p)
    valor = p * (p - l1) * (p - l2) * (p - l3)
    print(valor)
    raiz = math.sqrt(valor)
    area_escaleno = raiz
    perimetro_escaleno = l1 + l2 + l3


# SAÍDA

if equilatero:
        print(f'As medidas de {l1}, {l2} e {l3} referen-se a uma triângulo equilátero com {altura_equilatero:.2f} cm de altura, '
              f'{perimetro_equilatero:.2f} cm de perímetro e área de {area_equilatero:.2f} cm².')
elif isosceles:
    print(f'As medidas de {l1}, {l2} e {l3} referen-se a uma triângulo equilátero com {altura_isosceles:.2f} cm de altura, '
        f'{perimetro_isosceles:.2f} cm de perímetro e área de {area_isosceles:.2f} cm².')
elif escaleno:
    print(
        f'As medidas de {l1}, {l2} e {l3} referen-se a uma triângulo escaleno com seme perímetro de {p:.2f} cm, '
        f'{perimetro_escaleno:.2f} cm de perímetro e área de {area_escaleno:.2f} cm².')
else:
    print('Não é um triângulo. A medida do lado precisa ser menor que a soma dos outros dois lados.')
