"""
Escreva um algorítimo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior foi lido.
A quantidade de números a serem lidos deve ser fornecida pelo usuário.

"""


quantidade = int(input('Informe a quandidade de números a serem informados: '))

numeros = []


for n in range(quantidade):
    numeros.append(int(input(f'Informe o número{n+1}/{quantidade}: ')))
print(f'O maior número informado foi {max(numeros)} e ele foi informado {numeros.count(max(numeros))} vezes')
