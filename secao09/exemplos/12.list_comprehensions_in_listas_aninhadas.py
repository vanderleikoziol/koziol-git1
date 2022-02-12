listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(valor) for valor in lista] for lista in listas]

print('-='*20)

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]

print(tabuleiro)


print('-='*20)

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

print('-='*20)

print([['*' for i in range(1, 4)] for j in range(1, 4)])