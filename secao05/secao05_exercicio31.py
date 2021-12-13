"""
Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre qual
a classificação desta pessoa.
__________________________________________________________________________________________________
                                                       Peso
__________________________________________________________________________________________________
     ALTURA            Até 60                Entre 60 e 90 (inclusive)            Acima de 90
__________________________________________________________________________________________________
Menor que 1,20           A                               D                              G
De 1,20 a 1,70           B                               E                              H
Maior que 1,70           C                               F                              I
__________________________________________________________________________________________________

"""

altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))

if altura < 1.2:
    if peso < 60:
        print('Sua classificação é A')
    elif 60 <= peso <= 90:
        print('Sua classificação é D')
    else:
        print('Sua classificação é G')
elif 1.2 <= altura <= 1.7:
    if peso < 60:
        print('Sua classificação é B')
    elif 60 <= peso <= 90:
        print('Sua classificação é E')
    else:
        print('Sua classificação é H')
else:
    if peso < 60:
        print('Sua classificação é C')
    elif 60 <= peso <= 90:
        print('Sua classificação é F')
    else:
        print('Sua classificação é I')
