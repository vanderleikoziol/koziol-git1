"""
Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de erro
se a opção for inválida.
Escolha a opção:
1 => Soma de dois números.
2 => Diferença de dois números (maior pelo menor).
3 => Produto entre dois números.
4 => Divisão entre dois números (o denominador não pode ser zero).

"""

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

print('Escolha a opção:\n1. Para somar \n2. Para subtrair \n3. Para multiplicar \n4. para dividir.')

x = int(input('Digite a opção: '))

if x == 1:
    valor = n1 + n2
    print(f'A soma dos números é: {valor:.2f}')
elif x == 2:
    if n1 > n2:
        valor = n1 - n2
        print(f'A diferença dos números é: {valor:.2f}')
    else:
        valor = n2 - n1
        print(f'A diferença dos números é: {valor:.2f}')
elif x == 3:
    valor = n1 * n2
    print(f'O produto dos números é {valor:.2f}')
elif x == 4:
    if n2 > 0:
        valor = n1 / n2
        print(f'O resultado da divisão dos números é {valor:.2f}')
    else:
        print(f'Informe um denominador maior que zero.')