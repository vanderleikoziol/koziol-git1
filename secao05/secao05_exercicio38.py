"""
Uma data de nascimento de uma pessoa é fornecida através de três números inteiros: Dia, mês e ano.
Teste a validade desta data para saber se é uma data válida.
Teste de o dia fornecido é um dia válido: dia > 0, dia <= 28 para o mês de fevereiro (29 se for bissexto) dia <= 30 em
abril, junho, setembro e novembro, dia < 31 nos outros meses.
Teste a validade do ano: ano <= ano atual (use uma constante definida como valor igual a 2020)
Imprimir data válida ou data inválida no final da execução do programa.

"""

data = list(map(int, input('Informe a data conforme exemplo: 15 01 2021: ').split()))

dia = data[0]
mes = data[1]
ano = data[2]

valida = False

if ano < 2021:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 11 or mes == 12:
        if dia <= 31:
            valida = True
    elif mes == 4 or mes == 5 or mes == 9 or mes == 10:
        if dia <= 30:
            valida = True
    elif mes == 2:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            if dia <= 29:
                valida = True

if valida:
    print(f'A data {dia}/{mes}/{ano} é uma data de nascimento válida.')
else:
    print(f'A data {dia}/{mes}/{ano} não é uma data de nascimento válida.')
