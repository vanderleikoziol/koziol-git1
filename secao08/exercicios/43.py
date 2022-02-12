def vetor_sem_repeticaos843():
    import numpy as np
    from numpy.random import default_rng
    rng = default_rng()
    vetor = rng.choice(range(1, 99), size=(1, 10), replace=False)
    return f'O vetor sem repetição é => {np.sort(vetor)}'


print(vetor_sem_repeticaos843())
