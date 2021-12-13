"""
Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias.

Infantil A => 5 a 7 anos
Infantil B => 8 a 10 anos
Juvenil A => 11 a 13 anos
Juvenil B => 14 a 17 anos
Sênior => Maiores de 18 anos

"""


x = int(input('Informe a idade do nadador: '))


if 5 <= x <= 7:
    print('Infantil A')
elif 8 <= x <= 10:
    print('Infantil B')
elif 11 <= x <= 13:
    print('Juvenil A')
elif 14 <= x <= 17:
    print('Juvenil B')
elif x >= 18:
    print('Maiores de 18 anos')
else:
    print('Não tem idade para praticar natação.')
