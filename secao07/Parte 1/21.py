a = []
b = []
c = []
n = 0

for i in range(10):
    x = int(input(f'Informe o valor do vetor A: {n + 1}/10: '))
    y = int(input(f'Informe o valor do vetor B: {n + 1}/10: '))
    a.append(x)
    b.append(y)
    z = x - y
    c.append(z)
    n += 1
print(c)
