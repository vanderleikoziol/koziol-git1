def maior_fator_primo(n):
    """
Sabendo que o número 2 é o primeiro número primo, então inicializa com i = 2 e o maior fator = 0.
Sabendo que o 1 não é primo, então enquanto n (valor informado pelo usuário) for diferente de 1 eu verifico via um novo
while a seguinte condição:
1⁰ => abro uma função int e transformo (n / i) em string.
2⁰ => após transformar em string o inteiro vai ficar na posição [0] e o resto na posição [1].
3⁰ => realizo um split da string eliminando o ponto '.' e chamando a posição [1] que é o resto.
4⁰ => verifico se o resto é maior do que zero.
Enquanto o resto for maior do que zero vou incremento o i que está sendo usado para dividir o n e checando a
divisão n por i.
A hora que o resto for zero o maior fator será o i (incrementado) que iniciou valendo 2.
    :param n: número informado pelo usuário
    :return: maior fator primo deste número
    """
    i = 2
    maior_fator = 0
    while n != 1:
        while int(str(n / i).split('.')[1]) > 0:
            i += 1
        n = n / i
        maior_fator = i
    return maior_fator


f = int(input(f'Informe um valor maior do que zero: '))
if f > 0:
    print(f'O maior fator primo de {f} é {maior_fator_primo(f)} ')
else:
    print(f'o número {f} digitado é inválido.')

