vetor = []
cont = 0
for i in range(0, 50 + 1):
    x = (i + 5 * i) % (i + 1)
    cont += 1
    vetor.append(x)
print(vetor)
