import random
vetor = []
n = 0
while n < 10:
    vetor.append(random.randint(1, 10))
    n += 1
print(vetor)

vetor.sort()

print(vetor)
