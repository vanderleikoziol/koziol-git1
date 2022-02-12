from random import random
v = []
v1 = []
v2 = []

for i in range(10):
    v.append(int(input(f'Informe o valor {i + 1}/10: ')))
print(f'v = {v}')

for i, y in enumerate(v):
    if y % 2 == 0:
        v1.append(y)
    else:
        v2.append(y)
print(f'v1 = {v1}')
print(f'v2 = {v2}')

