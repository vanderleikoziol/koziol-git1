n = int(input('Digite um número: '))
vet = []
vetNum = []
for i in range(0, n):
    vetNum.clear()
    for y in range(0, i+1):
        vetNum.append(1)
    vet.insert(i, list(vetNum))
index = 0
for i in range(len(vet)):
    index = 1
    for x in range(len(vet[i])):
        if x < len(vet[i]) - 1:
            if i+1 < len(vet):
                vet[i+1][index] = sum(vet[i][x:x+2])
            index += 1
        print(vet[i][x], end=' ')
    print('')
