"""
Faça um programa que receba dois números. Calcule e mostre:
a) A soma dos números pares desse intervalo, incluindo os números digitados.
b) A multiplicação dos números impares desse intervalo, incluindo os digitados.

"""


soma = 0
multiplicacao = 1

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

for n in range(n1, n2 + 1, + 1):
    if n % 2 == 0:
        soma = soma + n
    else:
        multiplicacao = multiplicacao * n

print(f'A soma dos pares é: {soma}')
print(f'O produto dos impares é: {multiplicacao}')

