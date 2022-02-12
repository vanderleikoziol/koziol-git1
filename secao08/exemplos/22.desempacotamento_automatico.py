def soma_todos_numeros(*args):
    print(args)
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(3, 4, 5, 6))
numeros = [1, 2, 3, 4, 5, 6, 7]
print(soma_todos_numeros(*numeros))
