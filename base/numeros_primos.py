x = int(input('Informe um valor: '))
tot = 0
for i in range(1, x + 1):
    if x % i == 0:
        tot += 1
if tot == 2:
    print(f'O número {x} é primo!')
else:
    print(f'O número {x} não é primo!')
