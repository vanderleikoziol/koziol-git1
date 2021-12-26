"""
Faça um programa que leia um número indeterminado de idades de indivíduos (pare quando for informada a idade 0),
calcule a média desse grupo.

"""
soma = 0
cont = 0
media = 0
while True:
    x = int(input('Informe a idade: '))
    soma += x
    cont += 1
    media = soma / cont
    print(f'Total já lido: {cont}\nMédia: {media}')
    if x <= 0:
        break
