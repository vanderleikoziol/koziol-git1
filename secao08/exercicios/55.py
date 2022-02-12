def soma_elementos_matriz_s8_e55():
    import numpy as np
    from numpy.random import default_rng
    rng = default_rng(5)
    a = rng.choice(range(1, 20), size=(3, 3), replace=False)
    x = []
    y = 3
    for i in range(3):
        y -= 1
        for j in range(3):
            if i == j:
                x.append(a[i][j])
            if j == y:
                x.append(a[i][j])

    return f'{a}\nA soma dos elementos da DP e DS é => {sum(x)}'


print(soma_elementos_matriz_s8_e55())
