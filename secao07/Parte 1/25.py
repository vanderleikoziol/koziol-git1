vetor = []
valor = 0
n = 0
while valor < 100:
    if (n + 3) % 10 != 0 and n % 7 != 0:
        vetor.append(n)
        valor += 1
    n += 1
print(vetor)
print(len(vetor))
