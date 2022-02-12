from numpy.random import default_rng
rgn = default_rng()
matriz = rgn.choice(range(0, 99), size=(5, 5), replace=False)
print(matriz)
