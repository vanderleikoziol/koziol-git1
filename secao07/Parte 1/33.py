import random
x = []
n = 0
while n < 15:
    x.append(random.randint(0, 15))
    n += 1
print(f'O vetor sem eliminar indices com valor zero  é:{x}')

for p, y in enumerate(x):
    if y == 0:
        x.pop(p)
print(f'O vetor após eliminar indices com valor zero é:{x}')
