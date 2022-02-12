n = 0
x = []
while n < 10:
    y = int(input(f'Informe o valor {n+1}/10: '))
    n += 1
    x.append(y)

print(f'O vetor é: {x}')
print(f'O maior valor do vetor é: {max(x)}')
print(f'O menor valor do vetor é: {min(x)}')