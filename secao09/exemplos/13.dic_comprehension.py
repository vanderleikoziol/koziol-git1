numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(numeros)
print(quadrado)

print('-='*20)

numeros = [1, 2, 3, 4, 5]

quadrado = {valor: valor ** 2 for valor in numeros}
print(quadrado)
