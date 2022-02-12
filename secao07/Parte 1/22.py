a = []
b = []
c = []
n = 0
j = -1

for i in range(10):
    x = int(input(f'Informe o valor {n+1}/10 do vetor A: '))
    y = int(input(f'Informe o valor {n+1}/10 do vetor B: '))
    a.append(x)
    b.append(y)
    n += 1
    j += 1
    if j % 2 == 0:
        c .append(x)
    else:
        c.append(y)
print(a)
print(b)
print(c)
