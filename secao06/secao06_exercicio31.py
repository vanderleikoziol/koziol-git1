"""
Faça um programa que calcule e escreva o valor de S.

"""

x = 0
soma = 0
for i in range(0, 99 + 1):
    if i % 2 != 0:
        i = i
        x += 1
        soma += i / x

print(f'A soma é: {soma:.2f}')


