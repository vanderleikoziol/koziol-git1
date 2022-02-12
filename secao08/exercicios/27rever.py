import math


def exp(n, x):
    """
    O for para o valor de n (repete n vezes) e vai incrementar a soma de x elevado a i dividido pelo fatorial de !i.
    :param n: intervalo da função de Taylor => neste caso pede para n variar de 0 a 5.
    :param x: valor do ângulo em graus
    :return: o seno do ângulo informado em x
    """
    soma = 0
    for i in range(1, n + 1):
        soma += math.pow(x, i) / math.factorial(i)
    return soma


a = int(input("Informe o intervalo 'n' da função de Taylor =>  "))
b = float(input("Informe o valor do ângulo em graus =>  "))


print(f"O valor do seno desse angulo é: {exp(a, b):.4f}")
