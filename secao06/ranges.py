"""
É necessário conhecer o for para poder utilizar o range e conhecer o range para trabalhar melhor com for.

range => São utilizados para gerar sequências numéricas, não de forma aleatórias, mas sim de maneira especificada.

FORMA GERAIS:

Forma 1
range(valor_de_parada)
Observações: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)
for num in range(11):
    print(num)

Forma 2
range(valor_de_inicio, valor_de_parada)
Observações: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)
for num in range(5, 11):
    print(num)

Forma 3
range(valor_de_inicio, valor_de_parada, passo)
Observações: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)
for num in range(1, 10, 2):
    print(num)

Forma 4 (inverso da formula 3)
range(valor_de_inicio, valor_de_parada, passo)
Obs: valor_de_parada não inclusive (valor_de_inicio especificado pelo usuário, e passo especificado pelo usuário)
for num in range(10, 0, -1):
    print(num)
Usado para decrescer.
Note que se eu quiser chegar até zero basta substituir o zero por -1.

Observações:
Se eu precisar converter um range em lista.
lista = list(range(10))
print(lista)
"""

print('RANGES')
print('*' * 20)
print('Forma 1')
for num in range(11):
    print(num)
print('Forma 2')
for num in range(5, 11):
    print(num)
print('Forma 3')
for num in range(1, 10, 2):
    print(num)
print('Forma 4')
for num in range(10, 0, -1):
    print(num)
print('Converter um range em lista')
lista = list(range(10))
print(lista)
