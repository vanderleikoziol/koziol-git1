"""
Faça um programa que calcule o maior número palíndromo feito a partir do produto de dois números de 3 dígitos.
Ex. O maior palíndromo feito a partir do produto de dois números de dois dígitos é 9009 = 91 * 99.

"""


i = 0
j = 0
palindromo = 0
while i <= 999:
    j = i
    while j <= 999:
        x = str(i * j)
        x_inverso = x[::-1]
        if x == x_inverso:
            palindromo_x = int(x)
            if palindromo_x > palindromo:
                palindromo = palindromo_x
        j += 1
    i += 1
print(palindromo)

