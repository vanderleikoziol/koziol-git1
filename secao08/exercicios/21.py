def numeros_primos(n):
    """
    Enquanto o número informado pelo usuário for maior que 1 o cont vale 1 e vou fazer um for nesse número iniciando
    em 1. Se esse número informado pelo usuário for módulo de i que vai ser os números de 2, 3, 4, 5...até o valor de n
    conforme o for for rodando, o conta va somar 1 e passar a valer 2. Se o cont vale 2 a lista vai apender o número
    porque o número é primo. Lembrando que em cada rodada do for o cont volta a valer apenas 1 enquanto o n é - 1.
    :param n: número informado pelo usuário
    :return: quantidade de números primos abaixo do número informado
    """
    lista = []
    x = n
    while n > 1:
        cont = 1
        for i in range(1, n):
            if n % i == 0:
                cont += 1
        if cont == 2:
            lista.append(n)
        n -= 1
    return f'Há {len(lista)} números primos abaixo de {x}.\nOs números primos são => {sorted(lista)}'


print(numeros_primos(int(input(f'Informe um número: '))))
