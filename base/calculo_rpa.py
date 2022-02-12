"""
Funcionário x recebe por RPA e precisa recolher IR, INSS e ISS. A empresa negociou valor líquido e é necessário
encontrar o custo do funcionário.
"""
ir = 0
x = float(input('Informe o valor líquido a receber: '))

if 100 < x <= 1000:
    ir = x * (15 / 100)
    print(f'O valor de IR a pagar é: R$ {ir:.2f}.')
elif 1000 < x <= 2000:
    ir = x * (20 / 100)
    print(f'O valor de IR a pagar é: R$ {ir:.2f}.')
elif 2000 < x <= 3000:
    ir = x * (25 / 100)
    print(f'O valor de IR a pagar é: R$ {ir:.2f}.')
elif x > 3000:
    ir = x * (27.5 / 100)
    print(f'O valor de IR a pagar é: R$ {ir:.2f}.')
else:
    x = 0
    print(f'O valor de IR a pagar é: R$ {ir:.2f}.')


