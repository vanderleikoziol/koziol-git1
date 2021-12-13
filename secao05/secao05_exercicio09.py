"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário
imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.

"""

s = float(input('Informe o valor do salário: '))
p = float(input('Informe o valor da prestação: '))


i = p / s

if i > (20 / 100):
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
