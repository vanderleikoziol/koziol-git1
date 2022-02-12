def troque(a, b):
    primeira = b
    segunda = a
    return f'A primeira variável vale {primeira} e a segunda vale {segunda}'


x = int(input(f'Informe o valor de Primeira variável: '))
y = int(input(f'Informe o valor de segunda variável: '))

print(troque(x, y))
