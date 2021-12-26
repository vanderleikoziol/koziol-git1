"""
Faça um programa que conte os números primos que existem entre a e b, onde a e b são números informados pelo usuário.

"""


a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))

lista_primos = []
soma = 0

for x in range(a, b + 1):
    cont = 0

    for y in range(1, x + 1):
        if x % y == 0:
            cont += 1

    if cont == 2:
        lista_primos.append(x)
        soma = sum(lista_primos)

print(f'Lista de números primos => {lista_primos}')
print(f'Existem {len(lista_primos)} números primos entre {a} e {b}.')
print(f'A soma dos primos é: {soma}')


