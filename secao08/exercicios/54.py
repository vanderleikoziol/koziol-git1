def soma_elementos_matriz_s8_e54():
    import numpy as np
    from numpy.random import default_rng
    rng = default_rng(5)
    a = rng.choice(range(1, 20), size=(4, 4), replace=False)
    x = np.sum(a)
    return f'{a}\nA soma da matriz é => {x}'


print(soma_elementos_matriz_s8_e54())

