"""
Faça um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros números naturais.

"""
soma = 0
num = int(input('Informe um número: '))

for n in range(0, num + 1):
    if n > 0:
        soma = soma + n
        print(f'{n} => {soma}')
