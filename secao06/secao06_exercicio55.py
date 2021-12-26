"""
Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros números primos.

"""

n = int(input('Informe um número: '))

soma = 0
conta = 0
num = 2

while conta < n:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    if primo:
        soma += num
        conta += 1
    num += 1
print()
print(f'A soma dos números primos é: {soma}.')
