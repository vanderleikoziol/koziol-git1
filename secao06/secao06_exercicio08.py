"""
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

"""

maior = - 999
menor = 999

for n in range(1, 10 + 1):
    valor = int(input(f'Informe o número {n}/10 valor: '))
    if valor > 0:
        if valor > maior:
            maior = valor
    else:
        if valor < menor:
            menor = valor
print(f'O menor valor é {menor} e o maior valor é {maior}')
