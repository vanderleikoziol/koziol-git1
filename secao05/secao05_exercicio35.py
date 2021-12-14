"""
Leia uma data de termine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe naquele mês.
Note que fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.

"""
from datetime import date

dia = int(input('Dia: '))
mes = int(input('Mes: '))
ano = int(input('Ano: '))

valida = False

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31:
        valida = True
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
        valida = True
elif mes == 2:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        if dia <= 29:
            valida = True
if valida:
    print('Data Válida.')
else:
    print('Data Inválida.')
