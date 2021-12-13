"""
Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês. Imprima o valor
a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
ht => Número de horas trabalhadas
vh => Valor hora

"""

# Entrada


ht = int(input('Informe o número de horas trabalhadas: '))
vh = int(input('Informe o valor da hora trabalhada em R$ '))

# Processamento


total = ht * vh
valor = total + (total * (10 / 100))

# Saída


print(f'O valor a ser pago para o funcionário é R$ {valor:.2f}.')