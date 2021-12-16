"""
Escreva um programa que, dado o valor da veda imprima a comissão que deverá ser paga ao vendedor. Para calcular a
comissão, considere a tabela abaixo.

_________________________________________________________________________________
  VENDA MENSAL                                                  COMISSÃO
__________________________________________________________________________________
Valor >= R$ 100.000,00                                 R$ 700,00 + 16% das vendas.
Valor < R$ 100.000,00 e >= a R$ 80.000,00              R$ 650,00 + 14% das vendas.
Valor < R$ 80.000,00 e >= a R$ 60.000,00               R$ 600,00 + 14% das vendas.
Valor < R$ 60.000,00 e >= a R$ 40.000,00               R$ 550,00 + 14% das vendas.
Valor < R$ 40.000,00 e >= a R$ 20.000,00               R$ 500,00 + 14% das vendas.
Valor < R$ 20.000,00                                   R$ 400,00 + 14% das vendas.
__________________________________________________________________________________

"""


valor = int(input('Informe o valor da venda: '))


if valor >= 100_000:
    x = 700 + (valor * (16 / 100))
    print(f'O valor da comissão é: {x:.2f}')
elif 100_000 > valor >= 80_000:
    x = 650 + (valor * (14 / 100))
    print(f'O valor da comissão é: {x:.2f}')
elif 80_000 > valor >= 60_000:
    x = 600 + (valor * (14 / 100))
    print(f'O valor da comissão é: {x:.2f}')
elif 60_000 > valor >= 40_000:
    x = 550 + (valor * (14 / 100))
    print(f'O valor da comissão é: {x:.2f}')
elif 40_000 > valor >= 20_000:
    x = 500 + (valor * (14 / 100))
    print(f'O valor da comissão é: {x:.2f}')
elif 20_000 > valor > 0:
    x = 400 + (valor * (14 / 100))
    print(f'O valor da comissão é: {x:.2f}')
else:
    print('Você não tem comissão a receber.')
