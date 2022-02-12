v1 = []
v2 = []
v3 = {}
print('-' * 40)
for i in range(10):
    v1.append(int(input(f'Informe o valor {i + 1}/10 do vetor 1: ')))
    v2.append(int(input(f'Informe o valor {i + 1}/10 do vetor 2: ')))
    print('-' * 40)
print(f'O vetor 1 é: {v1}')
print(f'O vetor 2 é: {v2}')

x1 = set(v1)
x2 = set(v2)

v3 = x1.union(x2)
print(f'O vetor 3 é: {v3}')
