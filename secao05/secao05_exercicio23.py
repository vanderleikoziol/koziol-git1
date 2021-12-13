"""
Determine se um determinado ano é bissexto.Sendo que um ano é bissexto se for divisível por 400 ou se for divisível
por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996.
Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)

Logo, temos o código:

"""


ano = int(input('Ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Bissexto')
else:
    print('Não é bissexto')
