x = int(input('Informe um número: '))

t = 0

for i in range(1, x + 1):
    if x % i == 0:
        print('\033[33m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(x, t))

if t == 2:
    print('É Primo')
else:
    print('Não é Primo')