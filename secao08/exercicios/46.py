def vetor_s8_e46():
    import numpy as np
    from numpy.random import default_rng
    rng = default_rng()
    vetor = rng.choice(range(1, 99), size=(1, 20), replace=False)
    return f'O vetor é => {vetor}\nVetor inverso => {np.flip(vetor)}\nMédia vetor => {np.mean(vetor):.2f}'


print(vetor_s8_e46())
