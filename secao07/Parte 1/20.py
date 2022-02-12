from random import random

vetor = []
vetor_impar = []

for i in range(10):
    n = int(random() * 50)
    if n % 2 == 1:
        vetor_impar.append(n)
    vetor.append(n)
print(f'Vetor: {vetor}')
print(f'Vetor Impar: {vetor_impar}')

x = len(vetor_impar)

for i in range(10):
    if i < x:
        print(f'{vetor[i]} {vetor_impar[i]}')
    else:
        print(f'{vetor[i]}')
