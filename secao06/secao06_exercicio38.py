"""
Faça um programa que calcule o termo pitagórico a, b, c, para o qual a + b + c = 1000.
Um termo pitagórico é um conjunto de três números naturais, a, a, c, para o qual a ao quadrado mais b ao quadrado
é igual a c ao quadrado. 3**2 + 1**2 = 9 + 16 = 25 = 5**2.

Modelo bastante demorado

for a in range(1, 1000):
    if a <= 1000:
        for b in range(1, 1000):
            if a + b <= 1000:
                for c in range(1, 1000):
                    if a + b + c == 1000:
                        if a ** 2 == b ** 2 + c ** 2:
                            print(f'{a} + {b} = {c}')


"""

from math import sqrt
for a in range(1, 500):
    for b in range(1, 500):
        c = sqrt(a ** 2 + b ** 2)
        if a+b+c == 1000:
            print(f'{a}**2 + {b}**2 = {c}**2')

