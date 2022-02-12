def vetors843():
    import numpy as np
    from numpy.random import default_rng
    rng = default_rng()
    x = rng.choice(range(1, 99), size=(1, 30), replace=False)
    a = []
    b = []
    for i in range(1):
        for j in range(30):
            if x[i][j] % 2 == 0:
                a.append(x[i][j])
            else:
                b.append(x[i][j])
    return f'Vetor par   => {a}\nVetor impar => {b}'


print(vetors843())
