"""
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados pelo
 encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.
 n = número de dias
 sb = salário bruto
 sl = salário líquido

"""

# Entradas

n = int(input('Informe o número de dias trabalhados: '))


# Processamento


sb = n * 30
sl = sb - (sb * (8 / 100))

# Saída


print(f'O valor do salário líquido é {sl:.2f}.')