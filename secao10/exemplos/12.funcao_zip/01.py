lista1 =[1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)
print(type(zip1))

print('-='*30)

print(list(zip1))
zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))
zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))
zip1 = zip(lista1, lista2)
print(dict(zip1))

print('-='*30)
"""
O zip utiliza como parâmetro o menor iterável.
"""
lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

print('-='*30)

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}
zt = zip(tupla, lista, dicionario.values())
print(list(zt))

print('-='*30)

"""
Podemos também utilizar uma lista de tuplas.
"""
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))
