v1 = list(input(f'Informe o primeiro número: '))
v2 = list(input(f'Informe o segundo número: '))
v1.reverse()
v2.reverse()
v3 = []
count = 0
print(v1)
print(v2)

for i in range(5):
    y = (int(v1[i]) + int(v2[i])) + count
    if y >= 10:
        y -= 10
        v3.append(y)
        count = 1
    else:
        v3.append(y)
        count = 0
print(v3)
