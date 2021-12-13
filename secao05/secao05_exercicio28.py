"""
Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes médias de acordo com
o valor numérico digitado pelo usuário.

a) Geométrica => Raiz cúbica de x * y * z
b) Ponderada => ((x + 2) * (y + 3) * z) / 6
c) Harmônica => 1 / ((1 / x) + (1 / y) + (1 / z))
d) Aritimética => (x + y + z) / 3

"""

print('CALCULO DE MÉDIA')
print('_' * 20)

x = int(input('Informe o primeiro valor: '))
y = int(input('Informe o segundo valor: '))
z = int(input('Informe o terceiro valor: '))

print("Qual tipo de média você quer calcular? Informe:\n1 => Geométrica.\n2 => Ponderada.\n3 => Harmônica."
      "\n4 => Aritimética.")

t = int(input('Informe o tipo de média: '))

if t == 1:
    media = (x + y + z) ** (1 / 3)
    print(f'A média geométrica é: {media:.2f}.')
elif t == 2:
    media = ((x + 2) * (y + 3) * z) / 6
    print(f'A média ponderada é: {media:.2f}.')
elif t == 3:
    media = 1 / ((1 / x) + (1 / y) + (1 / z))
    print(f'A média harmônica é: {media:.2f}.')
elif t == 4:
    media = (x + y + z) / 3
    print(f'A média aritimética é: {media:.2f}.')
else:
    print('Informe uma referência válida.')
