n = 0
a = []
while n < 6:
    x = int(input(f'Informe o valor {n+1}/6: '))
    print(n)
    n += 1
    a.append(x)
simples = 0
for indice, n in enumerate(a):
    if indice == 0 or indice == 1 or indice == 5:
        simples += n

print(f'a) O vetor é: {a}.')
print(f'b) A soma das posições A[0], A[1] e A[5] é: {simples}')

a.pop(4)
a.insert(4, 100)
print(f'c) O vetor alterado na posição 4 é: {a}.')
print(f'd) O valor de cada vetor é:')
for elemento in a:
    print(elemento)
