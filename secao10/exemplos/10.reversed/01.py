lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

print(list(reversed(lista)))  # convertendo para lista
print(tuple(reversed(lista)))  # convertendo para tuple
print(set(reversed(lista)))  # convertendo para conjunto


for letra in reversed('Geek University'):
    print(letra, end='')
print('\n')
print(''.join(list(reversed('Geek University'))))

print('Geek University'[::-1])



