print('SOLUÇÃO COS LISTA')
vetor = []
n = 0

while n < 5:
    y = int(input(f'Informe o valor {n + 1}/5: '))
    n += 1
    vetor.append(y)
print(vetor)

print(f'O maior é: {max(vetor)} e está na posição {vetor.index(max(vetor))}')
print(f'O menor é: {min(vetor)} e está na posição {vetor.index(min(vetor))}')

print('*' * 60)


print('SOLUÇÃO COM DICT')
vetor = {}
n = 0

while n < 5:
    y = int(input(f'Informe o valor {n + 1}/5: '))
    n += 1
    vetor[n] = y
print(vetor)

print(f'O maior é: {max(vetor.values())} e está na posição {(max(vetor.values()))}')
print(f'O menor é: {min(vetor.values())} e está na posição {(min(vetor.values()))}')

print('*' * 60)

print('SOLUÇÃO COM TUPLE')

vetor = tuple(range(5, 10))
print(vetor)
print(f'O maior é: {max(vetor)} e está na posição {(vetor.index(max(vetor)))}')
print(f'O menor é: {min(vetor)} e está na posição {(vetor.index(min(vetor)))}')
