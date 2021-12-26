"""
Faça um programa que calcule a soma de todos os números primos abaixo de dois milhões.

"""


listaprimo = [True] * (2_000_000 + 1)

soma = 0
p = 2

while p + p <= 2_000_000: # Se não for alterado não é primo
    if listaprimo[p]: # Atualiza os multiplos
        i = p * 2
        while i <= 2_000_000:
            listaprimo[i] = False
            i += p
    p += 1
for i in range(2, 2_000_000, 1): # Soma dos primos
    if listaprimo[i]:
        soma += i
print(f'A soma de todos os números primos abaixo de 2 milhões é {soma}.')
