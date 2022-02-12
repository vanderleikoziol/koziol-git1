vetor = list(range(1, 10 + 1))
print(f'Vetor de 10 posições:{vetor}')

par = []

for n in vetor:
    if n % 2 == 0:
        par.append(n)
print(f'O vetor possui {len(par)} elementos pares.')



