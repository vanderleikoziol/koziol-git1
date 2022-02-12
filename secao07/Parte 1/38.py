x = []

for i in range(10):
    x.append(int(input(f'Informe o valor de {i + 1}/10: ')))
    x.sort()

print(x)
