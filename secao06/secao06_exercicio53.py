"""
Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado Triangulo de Floyd.
Para n = 6, temos:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21

"""

linha = 1
numero = 1
valor = 1
qtd_linhas = int(input('Informe o valor: '))
print('\n')
while linha <= qtd_linhas:
    while numero <= linha:
        if numero == 1:
            print(f'N = {str(linha).zfill(2)} | ', end='')
        print(str(valor).zfill(2), end='')
        print('', end=' ')
        numero += 1
        valor += 1
    print('\n', end='')
    numero = 1
    linha += 1


