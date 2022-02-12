def desvio_padraos8e45():
    import numpy as np
    from numpy.random import default_rng
    rng = default_rng()
    vetor = rng.choice(range(1, 99), size=(1, 30), replace=False)
    return f'O desvio padrão do vetor é => {np.std(vetor):.2f}'


print(desvio_padraos8e45())
