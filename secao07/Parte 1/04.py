valores = list(range(1, 9 + 1))
print(f'a) Vetor de 8 elementos: {valores}')
x = []
y = []


for indice, n in enumerate(valores):
    if indice == 2:
        x.append(n)
        print(f'b) O x foi lido na posição {indice} e o valor é: {n}')
    elif indice == 5:
        y.append(n)
        print(f'b) O y foi lido na posição {indice} e o valor é: {n}')

soma = x + y
print(f'd) A soma do x e Y é: {sum(soma)}')


