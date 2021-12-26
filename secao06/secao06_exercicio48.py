"""
Faça um programa que some os termos de valor par da sequência de Fibonacci, cujos calores não ultrapassem quatro
milhões.

"""
n1 = 0
n2 = 1
soma_pares = 0

while True:
    n3 = n1 + n2
    if n3 >= 4_000_000:
        print(soma_pares)
        break
    if n3 % 2 == 0:
        soma_pares += n3
    n1 = n2
    n2 = n3
    