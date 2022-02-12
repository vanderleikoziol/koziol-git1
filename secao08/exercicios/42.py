def media_vetors842():
    import numpy
    from numpy.random import default_rng
    rng = default_rng()
    vetor = rng.choice(range(1, 99), size=(1, 10), replace=False)
    return f'O vetor => {vetor} possui média de => {numpy.mean(vetor):.2f}'


print(media_vetors842())
