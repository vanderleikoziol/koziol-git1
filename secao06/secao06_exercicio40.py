"""
Elabore um programa que faça a leitura de vários números inteiros, até que digite um número negativo. O programa tem
que retornar o maior e o menor número lido.
"""


maior = -999
menor = 999

while True:
    valor = int(input('Informe um valor: '))
    if valor > 0:
        if valor > maior:
            maior = valor
    else:
        if valor < menor:
            menor = valor
    if valor < 0:
        break
print(f'O maior valor é {maior} e o menor valor é {menor}.')
