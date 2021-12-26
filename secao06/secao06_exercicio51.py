"""
Um funcionário recebe aumento anual. Em 1995 foi contratado por R$ 2.000,00. Em 1996 recebeu aumento de 1.5%. A partir
de 1997, os aumentos sempre correspondem ao dobro do ano anterior. Faça um programa que determine o salário atual do
funcionário.
"""


x = 2000 + (2000 * 0.015)
y = 0.015
n = 2021 - 1997
print(f'Aumento de: {y*100}% => R$ {x:.2f}')
for i in range(n):
    y = y * 2
    x = x + (x * y)
    print(f'Aumento de: {y*100:.0f}% => R$ {x:.2f}')




