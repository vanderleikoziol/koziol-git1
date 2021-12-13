"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a esse
número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.

"""


def switch(valor):
    switcher = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado",
    }

    return switcher.get(valor, "Não encontrei o dia correspondente.")


dia = int(input('Informe um número referente a um dia da semana: '))
print(switch(dia))
