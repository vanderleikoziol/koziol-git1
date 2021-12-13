"""
Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem
uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto de renda sobre o salário-base.

sb => salario base
sr => salário a receber
gt => gratificação
ir => Imposto de renda

"""

# Entradas

sb = int(input('Informe o valor do salário-base R$  '))


# Processamento

gt = sb * (5 / 100)
ir = sb * (7 / 100)
sr = sb + gt - ir

# Saída


print(f'O salário a receber é R$ {sr:.2f}')

