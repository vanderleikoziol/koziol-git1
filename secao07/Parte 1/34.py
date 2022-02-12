x = []
n = 0
while n < 10:
    y = (int(input(f'Informe o valor {n + 1}/10: ')))
    if y not in x:
        x.append(y)
        n += 1
    else:
        print(f'O número {y} já foi informado anteriormente, informe outro número.')
print(x)
