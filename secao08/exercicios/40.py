def vetor_inteiros():
    from numpy.random import default_rng
    rgn = default_rng(5)
    vetor = rgn.choice(range(0, 99), size=(1, 10), replace=False)
    matriz = []
    for i in range(1):
        for j in range(10):
            if vetor[i][j] % 2 == 0:
                matriz.append(vetor[i][j])

    return f'Há {len(matriz)} valores pares no vetor => {vetor} e os valores pares são => {matriz}'


print(vetor_inteiros())

