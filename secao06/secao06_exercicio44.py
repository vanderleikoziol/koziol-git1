"""
Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonancci até o primeiro número superior ao
lido. Exemplo: se o usuário informou o número 30, a sequência a ser impressa será 0 1 1 2 3 5 8 13 21 34.

"""

n = int(input('Informe um número: '))
t1 = 0
t2 = 1
cont = 3
print(t1, t2, end=' ')

while cont <= n:
    cont += 1
    t3 = t1 + t2
    print(t3, end=' ')
    t1 = t2
    t2 = t3
    if t3 > n:
        break


