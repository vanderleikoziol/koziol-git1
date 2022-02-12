def vetor(x, y, z):
    return {'x': x, 'y': y, 'z': z}


x = int(input('Digite o 1º número do Vetor 1: '))
y = int(input('Digite o 2º número do Vetor 1: '))
z = int(input('Digite o 3º número do Vetor 1: '))

dictV1 = vetor(x, y, z)

print()
x = int(input('Digite o 1º número do Vetor 2: '))
y = int(input('Digite o 2º número do Vetor 2: '))
z = int(input('Digite o 3º número do Vetor 2: '))

dictV2 = vetor(x, y, z)


def soma(dictV1, dictV2):
    res = []

    for k in dictV1:
        res.append(dictV1[k] + dictV2[k])

    return res


print()
print('Soma dos vetores: ', soma(dictV1, dictV2))
