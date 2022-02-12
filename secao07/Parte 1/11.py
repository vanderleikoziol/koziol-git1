vetor = []
negativo = []
positivo = []
n = 0
while n < 10:
    y = int(input(f'Informe o valor {n+1}/10: '))
    n += 1
    vetor.append(y)
    if y < 0:
        negativo.append(y)
    else:
        positivo.append(y)

print(f'A quantidade de números negativos é: {(len(negativo))}')
print(f'A soma dos positivos é: {(sum(positivo))}')


