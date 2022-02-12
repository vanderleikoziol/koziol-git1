x = []
n = 0

while n < 6:
    y = int(input(f'Informe o valor {n + 1}/6: '))
    if y % 2 == 0:
        x.append(y)
        n += 1
print(x)
x.reverse()
print(x)
