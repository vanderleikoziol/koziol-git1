"""
Faça um programa que apresente um menu de opções para cálculo das seguintes operações entre dois numeros.
Adição => Opção 01
Subtração => Opção 02
Multiplicação => Opção 03
Divisão => Opção 04
Saída => Opção 05

O programa deve possibilitar ao usuário a escolha da opção desejada, a exibição do resultado e a volta ao menu de
opções. O programa só termina quando for escolhida a opção de saída (opção 05).

"""


print('_'*35)
print('ESCOLHA UMA DAS OPÇÕES A SEGUIR')
print('_'*35)
print("Digite 1 para somar.\nDigite 2 para subtrair.\nDigite 3 para multiplicar.\nDigite 4 para dividir."
      "\nDigite 5 para sair.")
print('_'*35)
while True:
    x = (int(input('Informe sua opção: ')))
    print('_' * 35)
    if x == 5:
        print('Você saiu com sucesso.')
        break
    elif x > 5:
        print('Você deve escolher uma opção entre 1 e 5')
        print('_' * 35)
    else:
        n1 = (int(input('Informe o primeiro valor: ')))
        n2 = (int(input('Informe o primeiro valor: ')))
        if x == 1:
            n = n1 + n2
            print(f'A soma de {n1} e {n2} é: {n}')
            print('x' * 35)
            print('ESCOLHA UMA DAS OPÇÕES A SEGUIR')
            print('_' * 35)
            print('Digite 1 para somar.\nDigite 2 para subtrair.\nDigite 4 para dividir.\nDigite 5 para sair.')
            print('_' * 35)
        elif x == 2:
            n = n1 - n2
            print(f'A subtração de {n1} e {n2} é: {n}')
            print('x' * 35)
            print('ESCOLHA UMA DAS OPÇÕES A SEGUIR')
            print('_' * 35)
            print('Digite 1 para somar.\nDigite 2 para subtrair.\nDigite 4 para dividir.\nDigite 5 para sair.')
            print('_' * 35)
        elif x == 3:
            n = n1 * n2
            print(f'O produto de {n1} e {n2} é: {n}')
            print('x' * 35)
            print('ESCOLHA UMA DAS OPÇÕES A SEGUIR')
            print('_' * 35)
            print('Digite 1 para somar.\nDigite 2 para subtrair.\nDigite 4 para dividir.\nDigite 5 para sair.')
            print('_' * 35)
        elif x == 4:
            n = n1 / n2
            print(f'A divisão de {n1} por {n2} é: {n:.2f}')
            print('x' * 35)
            print('ESCOLHA UMA DAS OPÇÕES A SEGUIR')
            print('_' * 35)
            print('Digite 1 para somar.\nDigite 2 para subtrair.\nDigite 4 para dividir.\nDigite 5 para sair.')
            print('_' * 35)




