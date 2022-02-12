vetor = []
x = 0

while x < 10:
    p = int(input(f'Informe o valor {x+1}/10 para o vetor: '))
    x += 1
    vetor.append(p)

print(f'O vetor é: {vetor}')
for indice, p in enumerate(vetor):
    if p == max(vetor):
        print(f'O maior valor é: {(max(vetor))} e está na posição: {(vetor.index(p))} do vetor')




