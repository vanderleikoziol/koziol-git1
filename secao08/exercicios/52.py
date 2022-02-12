def transposta_s8_e52():
    import numpy as np
    from numpy.random import default_rng
    rng = default_rng(5)
    a = rng.choice(range(1, 20), size=(3, 3), replace=False)
    b = np.transpose(a)

    return f'{a}\n{b}'


print(transposta_s8_e52())

