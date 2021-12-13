"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem 'Número Inválido'. Se o número for positivo,
calcular o logaritimo deste número.
"""
import math


n = int(input('Informe o número: '))

if n < 0:
    print('Número inválido')
else:
    log = math.log(n)
    print(f'O log de {n} é {log:.2f}.')

