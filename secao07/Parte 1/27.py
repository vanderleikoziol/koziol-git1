lista = []
cont = 0
i = 1
n = 0
while len(lista) < 10:
    lista.append(int(input(f'Informe o valor {n + 1}/10: ')))
    n += 1
print(lista)

for p, y in enumerate(lista):
    while i <= y:
        if y % i == 0:
            cont += 1  # vou incrementar o cont somente se o y for divisível pelo número até ele.
            i += 1
        elif y % i != 0:
            i += 1
    if cont == 2:
        print(f'O número {y} é primo e está na posição {p} da lista.')
        cont = 0  # necessário para indicar o inicio
        i = 1  # necessário para indicar o inicio
    elif cont != 2:
        cont = 0  # necessário para continuar contando se for != de 2
        i = 1  # necessário para continuar contando se for != de 2


