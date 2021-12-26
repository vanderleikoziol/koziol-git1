menor = 999
maior = - 999
i = 1

while i < 11:
    n = int(input(f'Informe o {i}/10: '))
    i += 1
if n > maior:
    maior = n
elif n < menor:
    menor = n
print(f'O maior é {maior} e o menor é {menor}.')




