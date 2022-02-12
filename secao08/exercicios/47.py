def maior_que_10_s8_e47():
    import collections
    from numpy.random import default_rng
    rng = default_rng()
    vetor = rng.choice(range(1, 20), size=(4, 4), replace=False)
    a = []
    for i in range(4):
        for j in range(4):
            if vetor[i][j] > 10:
                a.append(vetor[i][j])
    return f'Há {len(a)} elementos maiores que 10 no array\n{vetor}.\nSão eles => {a}'


print(maior_que_10_s8_e47())
