import random
a = set(random.sample(range(0, 100), 10))
b = set(random.sample(range(0, 100), 10))


def uniao_vetor(x, y):
    c = a.union(b)
    return f'A união de:\nConjunto a => {a}\nConjunto b => {b}\nResulta no:\nConjunto c => {c}'


print(uniao_vetor(a, b))
