# Exemplo 1 => utilizando o loop comum
numeros = [1, 2, 3, 4, 5]
print(numeros)
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

#  Exemplo 2 => utilizando o list comprehension

print([numero * 2 for numero in numeros])
