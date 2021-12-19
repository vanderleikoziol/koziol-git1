"""
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.

"""
soma = 0
for n in range(50):
    if n % 2 == 0:
        soma = soma + n
        print(n)
print(f'A soma dos 50 primeiros números pares é {soma}.')

