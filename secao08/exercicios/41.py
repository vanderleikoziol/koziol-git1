def vetors842():
    import numpy as np
    from numpy.random import default_rng
    rng = default_rng()
    vetor = rng.choice(range(0, 99), size=(1, 2), replace=False)
    return f'O maior valor no vetor => {vetor} é => {np.amax(vetor)}'


print(vetors842())
