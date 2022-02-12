def fatorial(valor):
    """
    Exemplo de de cálculo do fatorial 5 que é 120 => (5 * 1 = 5)=>(5 * 2 = 10)=>(10 * 3 = 30)=>(30 * 4 = 120)
    Se o valor for menor que zero não há fatorial e se for =  a zero o fatorial de zero é 1.
    Então, enquanto o valor for diferente de 1 vou multiplicar o result pelo valor.
    Veja exemplo para 5!
    1⁰. result = (valor = 5 * result = 1) => result = 5 e o valor 5 - 1 = passa a ser 4
    2⁰. result = (valor = 4 * result = 5) => result = 20 e o valor 4 - 1 = passa a ser 3
    3⁰. result = (valor = 3 * result = 20) => result = 60 e o valor 3 - 1 = passa a ser 2
    4⁰. result = (valor = 2 * result = 60) => result = 120 e o valor 2 - 1 = passa a ser 1
    Quando o valor passa a ser 1 ele sai fora do while, pois só diferente de 1 entra na condição.
    :param valor: número informado pelo usuário para calcular o fatorial
    :return: o fatorial do número
    """
    result = 1
    x = valor
    if valor < 0:
        return 'Valor inválido.'
    elif valor == 0:
        return f'O fatorial de {x} é 1'
    while valor != 1:
        result = result * valor
        valor = valor - 1
    return f'O fatorial de {x} é {result}'


num = int(input('Informe um número para saber qual é seu fatorial:'))
print(fatorial(num))
