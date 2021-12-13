"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada.
Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.
 a => altura do degrau
 b => Objetivo do usuário
 x => número de degraus
"""

# Entradas


a = float(input('Informe a altura do degrau em metros: '))
b = float(input('Informe a altura que o usuário deseja alcançar em metros: '))

# Processamento

x = b / a

# Saída


print(f'Para atingir a altura de {b:.0f} metros o usuário deverá subir {x:.0f} degraus')

