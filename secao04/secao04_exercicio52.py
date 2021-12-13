"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um
deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima
 quanto cada um ganharia do prêmio com base no valor investido.

"""

# Entrada


j1 = int(input('Informe o valor investido pelo primeiro jogador: R$ '))
j2 = int(input('Informe o valor investido pelo segundo jogador: R$ '))
j3 = int(input('Informe o valor investido pelo terceiro jogador: R$ '))
p = int(input('Informe o valor do prêmio: R$ '))

# Processamento


soma = j1 + j2 + j3

f1 = j1 / soma
f2 = j2 / soma
f3 = j3 / soma

vj1 = p * f1
vj2 = p * f2
vj3 = p * f3

# Saída


print(f'O primeiro jogador investiu R$ {j1:.2f}, o valor do prêmio foi R$ {p} e receberá R$ {vj1:.2f} de prêmio.')
print(f'O segundo jogador investiu R$ {j2:.2f}, o valor do prêmio foi R$ {p} e receberá R$ {vj2:.2f} de prêmio.')
print(f'O terceiro jogador investiu R$ {j3:.2f}, o valor do prêmio foi R$ {p} e receberá R$ {vj3:.2f} de prêmio.')
