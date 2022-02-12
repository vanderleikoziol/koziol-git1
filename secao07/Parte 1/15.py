import xmlrpc.client

vetor = []
n = 0

while n < 20:
    y = int(input(f'Informe o valor {n+1}/20: '))
    n += 1
    vetor.append(y)
print(vetor)

novo = set(vetor)

vetor2 = list(novo)
print(vetor2)

vetor2.sort()

print(vetor2)

