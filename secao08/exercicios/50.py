def diagonal_principals8_e50():
    import collections
    from numpy.random import default_rng
    rng = default_rng(5)
    vetor = rng.choice(range(1, 20), size=(3, 3), replace=False)
    a = []
    for i in range(3):
        for j in range(3):
            if i == j:
                a.append(vetor[i][j])
    return f'O vetor é\n{vetor}\nA soma dos elementos da diagonal principal é => {sum(a)}'


print(diagonal_principals8_e50())
