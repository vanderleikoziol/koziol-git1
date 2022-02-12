import random

n = 0
notas = []

while n < 15:
    num = random.randint(0, 10)
    notas.append(num)
    n += 1

len(notas)
media = sum(notas) / len(notas)

notas = "|".join(map(str, notas))
print(f'A média geral das notas {notas} é: {media:.2f}')

