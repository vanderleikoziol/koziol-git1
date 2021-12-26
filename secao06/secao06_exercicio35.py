"""
Faça um programa que some os números impares contidos em um intervalo definido pelo usuário. O usuário define o valor
inicial do intervalo e o valor final deste intervalo. Caso o usuário digite um intervalo inválido (começando por um
valor maior que o valor final) deve ser escrito uma mensagem de erro na tela. "Intervalo de valores inválidos" e o
programa termina.
Exemplo de tela de saída: Digite o valor inicial e final: 5 10
Soma dos impares deste intervalo: 21

"""

soma = 0
n = 0
x = list(map(int, input('Digite o valor inicial e valor final: ').split()))

if x[0] > x[1]:
    print('Intervalo de valores inválido')
else:
    for i in range(x[0], x[1]):
        n += i
        if i % 2 != 0:
            soma += i
    print(f'A soma é: {soma}')
