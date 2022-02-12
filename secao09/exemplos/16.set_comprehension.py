
numeros = {num for num in range(1, 7)}

print(numeros)

print('-='*30)

numeros = {x ** 2 for x in range(10)}
print(numeros)

print('-='*30)

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

print('-='*30)

letras = {letra for letra in 'Geek University'}
print(letras)
