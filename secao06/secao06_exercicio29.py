"""
Escreva um programa para calcular o valor da serie, para 5 termos.
S = 0 + 1/2! + 2/4! + 3/6! + ...

"""


from math import factorial
f = 1
numerador = 0
denominador = 0
cont = 1
serie = 0
while cont <= 5:
    denominador = denominador + 2  # denominador vai ser sempre um numero par
    f = factorial(denominador)
    numerador = numerador + 1
    serie += (numerador / f)
    cont = cont + 1
    print(f'{numerador}/{f} = {serie:.2f}')
print(f'o valor final da serie é: {serie:.4f}')
