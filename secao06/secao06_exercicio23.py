"""
Faça um algorítimo que leia um número positivo e imprima seus divisores.

"""
n = int(input('Informe um número: '))
for divisor in range(1, n + 1):
    if n % divisor == 0:
        print(divisor)
        