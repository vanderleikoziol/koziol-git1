dicionario = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
              9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
x = int(input(f'Informe o dia: '))
y = int(input(f'Informe o mês: '))
z = int(input(f'Informe o ano com 4 dígitos: '))


def data(dia, mes, ano):
    print(f'{dia} de {dicionario.get(mes)} de {ano}')


data(x, y, z)
