x = []
n = 0
while n < 6:
    y = int(input(f'Informe o valor {n+1}/6: '))
    n += 1
    x.append(y)
print(x)

x.reverse()
print(x)
