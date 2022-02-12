import random
vetor = []
n = 0

while n < 11:
    vetor.append(random.randint(0, 11))
    n += 1
print(f'Vetor => {vetor}')
print(f'Até a posição 5=> {vetor[0:5]}')
print(f'Até a posição 5 em ordem crescente => {sorted(vetor[0:5])}')
print(f'Da posição 5 até a 11=> {vetor[5:]}')
print(f'Da 5 até a 11 invertida=> {vetor[5:][::-1]}')
print(f'Da 5 até a 11 invertida e em ordem crescente => {sorted(vetor[5:][::-1])}')
print(f'Conforme solicitado no exercício => {sorted(vetor[0:5]) + vetor[5:][::-1]}')

