"""
O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu salário.
Carlos gosta de fazer aplicações na cardeneta de poupança e vai aplicar seu salário integralmente nela, pois está
rendendo 2% ao mês. João aplicará seu salário integramente no fundo de renda fixa, que está rendendo 5% ao mês.
Construa um programa que deverá calcular e mostrar  a quantidade de meses necessários para que o valor pertencente a
João iguale ou ultrapasse o valor pertencente a Carlos. Teste com outros valores para as taxas.
Salário joão = 1/3 do salário do Carlos
Carlos aplica a 2% am
João aplica a 5% am
Em quantos meses valor de João Ultrapassa o de carlos?

"""


x = int(input('Informe o valor do salário de Carlos: '))
y = x * (1 / 3)
cont = 0
while True:
    x = x + (x * (2 / 100))
    y = y + (y * (5 / 100))
    dif = y - x
    cont += 1
    if y >= x:
        break
print(f'a) Após {cont} meses\nb) João terá um montante de:R$ {y:.2f}\nc) Carlos terá um montante de:R$ {x:.2f}.'
      f'\nd) João terá um valor de R$ {dif:.2f} superior ao de Carlos.')
