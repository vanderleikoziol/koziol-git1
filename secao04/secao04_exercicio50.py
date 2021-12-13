"""
Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.

"""

from datetime import datetime
import datetime

# Entrada


x = int(input('Informe sua idade: '))

# Processamento


year = datetime.date.today().year

# Saída


print(f' A pessoa tem {x} anos e nasceu em {year - x}')
