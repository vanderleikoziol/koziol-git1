"""
Faça um algorítimo que encontre o primeiro multiplo de 11, 13 ou 17 após um número dado.

"""


while True:
    try:
        num = int(input('Informe um número: '))
        if num % 11 == 0:
            print(f'O número {num} é múltiplo de 11')
            break
        elif num % 13 == 0:
            print(f'O número {num} é múltiplo de 13.')
            break
        elif num % 17 == 0:
            print(f'O número {num} é múltiplo de 17.')
            break
        else:
            print('Continue informando números, condição de parada números multiplos de 11, 13 ou 17.')
    except valueError:
        print('Você digitou um número inválido')