"""
Faça um programa que determine e mostre os cinco primeiros múltiplos de três, considerando números maiores do zero.

"""
t = 0
for n in range(3, 100):
    if n % 3 == 0:
        print(n)
        t = t + 1
        if t == 5:
            break


