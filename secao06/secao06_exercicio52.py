"""
Escreva um programa que receba como entrada o valor de saque realizado pelo cliente de um banco e retorne quantas notas
de cada valor serão necessárias para atender ao saque com a menor quantidade possível. Serão utilizadas notas de 100, 50,
20, 10, 5, 2 e 1 real.

"""

notas = [1, 2, 5, 10, 20, 50, 100]
valor_saque = int(input('Informe o valor do saque: '))
notas_saque = []
notas .sort(reverse=True)
print(notas)

for i in range(len(notas)):
    while valor_saque - notas[i] >= 0:
        valor_saque -= notas[i]
        notas_saque.append(notas[i])
print(notas_saque)
