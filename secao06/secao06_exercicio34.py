"""
Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20. Exemplo: 2.520 é o menor número
que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto.

"""

i = 1
j = 1

while j <= 20:
    if i % j == 0:
        j = j + 1
    else:
        i = i + 1
        j = 1
print(i)


