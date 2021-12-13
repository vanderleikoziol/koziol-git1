"""
Faça um programa que receba três números e mostre-os em ordem crescente.

"""


lista = []

for n in range(3):
    n = int(input(f'Informe o valor para N{n+1}: '))
    lista.append(n)

print()
lista.sort()
print(lista)
"""
Para imprimir a lista sem colchetes usei a função str.
"""
lista_str = str(lista)[1:-1]
print(lista_str)
"""
Outra forma é converter cada elemento da lista em string e usar a função join().
"""

nova_lista = [str(a) for a in lista]
print(','.join(nova_lista))
