vetor = []
n = 0

while n < 5:
    x = float(input(f'Informe o valor {n+1}/5: '))
    n += 1
    vetor.append(x)
print(f'Informe:\n0 => sair\n1 => Mostrar vetor na ordem direta.\n2 => Mostrar vetor na ordem inversa.')
y = int(input(f'Informe o código: '))

while y > 2 or y < 0:
    print('Código inválido')
    y = int(input(f'Informe o código: '))
if y == 1:
    print(vetor)
elif y == 2:
    vetor.reverse()
    print(vetor)
elif y == 0:
    exit()
