def soma_secundaria_s8_e51():
    from numpy.random import default_rng
    rng = default_rng(5)
    vetor = rng.choice(range(1, 20), size=(3, 3), replace=False)
    a = []
    x = 3
    for i in range(3):
        x -= 1
        for j in range(3):
            if j == x:
                a.append(vetor[i][j])
    return f'A soma da diagonal secundária é => {sum(a)}\n{vetor}'


print(soma_secundaria_s8_e51())
