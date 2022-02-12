vetor = []
n = 0

while n < 10:
    y = int(input(f'Informe o valor {n+1}/10: '))
    n += 1
    if y > 0:
        vetor.append(y)
    else:
        vetor.append(0)
print(vetor)
