"""
Escreva um programa na tela, de 1 até 100, de 1 em 1,3 vezes. A primeira vez deve usar a estrutura de repetição for,
a segunda while, e a terceira do while.

"""

print('Repetição com for')

for n in range(1, 101):
    if n == 101:
        break
    else:
        print(n)

print('Repetição com while')
n = 1
while n <= 100:
    print(n)
    n = n + 1
