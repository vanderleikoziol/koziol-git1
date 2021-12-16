"""
Uma empresa decide dar aumento aos seus funcionários de acordo com uma tabela que considera o salário atual e o tempo
de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente maior do que os
funcionários com salário maior, e conforme o tempo de serviço da empresa, cada funcionário irá receber bônus Fictional
de salário. Faça um programa que leia:

a) Valor do salário atual do funcionário.
b) O tempo de serviço desse funcionário na empresa (número de ano de trabalho na empresa).
Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final
reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.

  SALÁRIO ATUAL             REAJUSTE(%)                 TEMPO DE SERVIÇO           BÔNUS
  Até R$ 500.00                 25%                      Abaixo de 1 ano         Sem bônus
  Até R$ 1000.00                20%                      De 1 a 3 anos           R$ 100.00
  Até R$ 1500.00                15%                      De 4 a 6 anos           R$ 200.00
  Até R$ 2000.00                10%                      De 7 a 10 anos          R$ 300.00
  Acima de R$ 2000.00           Sem reajuste             Mais de 10 anos         R$ 500.00

"""

x = float(input('Informe o valor do salário: R$ '))
y = int(input('Informe o tempo de serviço em anos: '))

ref = False
reajuste = True
bonus = True

if x <= 500:
    if y < 1:
        r = x + (x * (25 / 100))
        ref = True
        bonus = False
    elif 1 <= y <= 3:
        r = x + (x * (20 / 100)) + 100
        ref = True
    elif 4 <= y <= 6:
        r = x + (x * (15 / 100)) + 200
        ref = True
    elif 7 <= y <= 10:
        r = x + (x * (10 / 100)) + 300
        ref = True
    else:
        r = x + 500
        ref = True
        reajuste = False
elif 500 < x <= 1000:
    if y < 1:
        r = x + (x * (25 / 100))
        ref = True
        bonus = False
    elif 1 <= y <= 3:
        r = x + (x * (20 / 100)) + 100
        ref = True
    elif 4 <= y <= 6:
        r = x + (x * (15 / 100)) + 200
        ref = True
    elif 7 <= y <= 10:
        r = x + (x * (10 / 100)) + 300
        ref = True
    else:
        r = x + 500
        ref = True
        reajuste = False
elif 1000 < x <= 1500:
    if y < 1:
        r = x + (x * (25 / 100))
        ref = True
        bonus = False
    elif 1 <= y <= 3:
        r = x + (x * (20 / 100)) + 100
        ref = True
    elif 4 <= y <= 6:
        r = x + (x * (15 / 100)) + 200
        ref = True
    elif 7 <= y <= 10:
        r = x + (x * (10 / 100)) + 300
        ref = True
    else:
        r = x + 500
        ref = True
        reajuste = False
elif 1500 < x <= 2000:
    if y < 1:
        r = x + (x * (25 / 100))
        ref = True
        bonus = False
    elif 1 <= y <= 3:
        r = x + (x * (20 / 100)) + 100
        ref = True
    elif 4 <= y <= 6:
        r = x + (x * (15 / 100)) + 200
        ref = True
    elif 7 <= y <= 10:
        r = x + (x * (10 / 100)) + 300
        ref = True
    else:
        r = x + 500
        ref = True
        reajuste = False
else:
    if y < 1:
        r = x + (x * (25 / 100))
        ref = True
        bonus = False
    elif 1 <= y <= 3:
        r = x + (x * (20 / 100)) + 100
        ref = True
    elif 4 <= y <= 6:
        r = x + (x * (15 / 100)) + 200
        ref = True
    elif 7 <= y <= 10:
        r = x + (x * (10 / 100)) + 300
        ref = True
    else:
        r = x + 500
        ref = True
        reajuste = False

if ref:
    if not bonus:
        print(f'O valor do seu salário reajustado é: {r:.2f} e você não tem direito a bônus.')
    elif not reajuste:
        print(f'O valor do seu salário reajustado é: {r:.2f} e você não tem direito a reajuste.')
    else:
        print(f'O valor do seu salário reajustado é: {r:.2f}')
