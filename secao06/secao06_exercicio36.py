"""
Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais e o quadrado da
soma.
a) A soma dos quadrados dos dez primeiros números naturais é => 385.
b) O quadrado da soma é => 3025
c) A diferença da soma dos quadrados é => 2640

"""

x = 0
y = 0
for i in range(0, 100 + 1, 1):
    x += i ** 2
    y += i
y = y ** 2
z = y - x

print(f'A soma dos quadrados é: {x}')
print(f'O quadrado da soma é: {y}')
print(f'A diferença é: {z}')
