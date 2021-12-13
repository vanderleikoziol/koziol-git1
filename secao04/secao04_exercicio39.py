"""
A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
Sendo a quantia total:
a) O primeiro ganhador receberá 46%.
b) O segundo ganhador receberá 32%.
c) O terceiro ganhador receberá o restante.

Calcule e imprima a quantia ganha por cada um dos ganhadores.

"""

# Entrada


# Processamento


q = 780000.00
g1 = q * (46 / 100)
g2 = q * (32 / 100)
g3 = q * (100 - 46 - 32) / 100
soma = g1 + g2 + g3

# Saída


print(f'O montante de {soma:.2f} será dividido em:')
print(f'1. O primeiro ganhador receberá {g1:.2f}.')
print(f'2. O segundo ganhador receberá {g2:.2f}.')
print(f'3. O terceiro ganhador receberá {g3:.2f}.')
