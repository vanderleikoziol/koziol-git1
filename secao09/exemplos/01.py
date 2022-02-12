numeros = [1, 2, 3, 4, 5]

res1 = [numero * 10 for numero in numeros]
res2 = [numero / 2 for numero in numeros]


print(res1)
print(res2)


def funcao(valor):
    return valor * valor


res3 = [funcao(numero) for numero in numeros]

print(res3)
