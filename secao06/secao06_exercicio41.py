"""
Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos pelo usuário via teclado.
Este programa fica pedindo esses valores e calculando até que o usuário entre com um valor para a resistência igual a
zero.
          R1 * R2
    R = ___________
          R1 + R2
"""


while True:
    r1 = int(input('Informe o valor de R1: '))
    r2 = int(input('Informe o valor de R1: '))
    r = (r1 * r2) / (r1 + r2)
    print(f'O valor é {r:.6f}')
    if r1 <= 0 or r2 <= 0:
        break
