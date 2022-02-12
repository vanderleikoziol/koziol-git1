from numpy.random import default_rng
rng = default_rng()
matriz = rng.choice(range(1, 20), size=(4, 4), replace=False)
print(matriz)