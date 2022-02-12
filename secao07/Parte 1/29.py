lista = []
pares = []
impares = []

for i in range(6):
    lista.append(int(input(f'Informe o valor {i + 1}/6: ')))
for i, y in enumerate(lista):
    if y % 2 == 0:
        pares.append(y)
    else:
        impares.append(y)
print(f'Os números são: {lista}')
print(f'Os números pares são: {pares}')
print(f'Os números impares são: {impares}')
print(f'A soma dos pares é: {sum(pares)}')
print(f'A quantidade de impares é: {len(impares)}')
