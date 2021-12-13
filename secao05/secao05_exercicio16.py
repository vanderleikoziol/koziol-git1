"""
Usando switch escreva um programa que leia um número inteiro entre 1 e 12 e imprima o mês correspondente a este
número. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.

"""


def switch(numero):
    switcher = {
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro',
    }
    return switcher.get(numero, 'Mês não identificado')


mes = int(input('Informe um número referente ao mês: '))
print(switch(mes))
