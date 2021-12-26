"""
Faça um programa que some os números primos existentes entre a e b, onde a e b são números informados pelo usuário.

"""


a = int(input('Informe um número: '))
b = int(input('Informe um número: '))

lista = []
soma = 0

for x in range(a, b + 1):
    cont = 0
    for y in range(1, x + 1):
        if x % y == 0:
            cont += 1


    if cont == 2:
        lista.append(x)
        soma = sum(lista)
print(lista)
print(soma)
