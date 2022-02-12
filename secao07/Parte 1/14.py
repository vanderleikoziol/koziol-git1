vetor = []
x = []
n = 0

while n < 10:
    y = int(input(f'Informe o valor de {n + 1}/10: '))
    n += 1
    vetor.append(y)
    if vetor.count(y) > 1:
        if n not in x:
            x.append(y)
z = sum(x)

x = ','.join(map(str, x))

if z > 0:
    print(f'Há valores repetidos no vetor: {vetor} e os valores são: {x}.')
else:
    print(f'Não há valores repetidos no vetor: {vetor}.')
    