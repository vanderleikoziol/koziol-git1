"""
Faça um programa que leia vários números, calcule e mostre:
a => A soma dos números digitados.
b => A quantidade de números digitados.
c => A média dos números digitados.
d => O maior número digitado.
e => O menor número digitado.
f => A média dos números pares.

"""


soma = 0
cont = 0
media = 0
maior = -999
menor = 999
cont_par = 0
soma_par = 0
media_par = 0

x = int(input('Informe um valor: '))

while x != 0:
    x = int(input('Informe um valor: '))
    soma += x
    cont += 1
    media = soma / cont
    if x > 0:
        if x > maior:
            maior = x
        else:
            if x < menor:
                menor = x
    if x % 2 == 0:
        cont_par += 1
        soma_par += x
        media_par = soma_par / cont_par
print(f'a) A soma é => {soma}\nb) A quantidade é => {cont}\nc) A média é => {media}\nd) O maior é => {maior}\ne) '
      f'O menor é => {menor}\nf) A média dos pares é => {media_par}')
