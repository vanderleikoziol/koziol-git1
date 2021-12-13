"""
Faça um programa que leia duas notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas
notas. Uma nota válida deve ser, obrigatóriamente, um valor entre 0.0 e 10.0. Onde, caso a nota não possua um valor
válido, este fato deve ser informado ao usuário e o programa termina.

"""
# Entradas


n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a primeira nota: '))

if n1 < 0.0 or n1 > 10.0:
    print("Nota inválida.")
elif n2 < 0.0 or n2 > 10.0:
    print("Nota inválida.")
else:
    media = (n1 + n2) / 2
    print(f'A media é {media:.2f}.')
