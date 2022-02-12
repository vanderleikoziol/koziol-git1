def fatorial_exponencial(n):

    x = n ** (n-1)

    for i in range(n-2, 0, -1):

        x **= (n**i)

    return x


n = int(input('Digite um número positivo maior que 0: '))

if n > 0:

    print(f'Fatorial exponêncial de {n} = {fatorial_exponencial(n)}')

else:

    print('Número inválido!')

