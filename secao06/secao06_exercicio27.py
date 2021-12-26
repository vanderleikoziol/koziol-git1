"""
Em matemática, o número harmônico designado por H(n) define-se como sendo a soma da serie harmónica:
H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).

"""

termos = int(input('Informe a quantidade de termos: '))

h = 1

for n in range(1, (termos + 1)):
    h = h + (1 / (n + 1))

print(f'H{termos} vale {h:.2f}')

