import random
vet = []
for i in range(3):
    vet.append(list(random.sample(range(0, 20), 3)))
for l in range(len(vet)):
    for c in range(len(vet)):
        print(vet[l][c], end=' ')
    print('')
print()
for l in range(len(vet)):
    for c in range(len(vet)):
        print(vet[c][l], end=' ')
    print('')
