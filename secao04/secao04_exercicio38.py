"""
Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.

"""

# Entradas
salario = int(input('Informe o valor do salário: '))


# Processamento


novo_salario = salario + (salario * (25 / 100))

# Saída


print(f'O novo salário é: {novo_salario:.2f}.')
