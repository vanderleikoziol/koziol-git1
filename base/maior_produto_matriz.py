import numpy as np

lin1 = np.array([8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8])
lin2 = np.array([49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0])
lin3 = np.array([81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65])
lin4 = np.array([52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91])
lin5 = np.array([22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80])
lin6 = np.array([24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50])
lin7 = np.array([32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70])
lin8 = np.array([67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21])
lin9 = np.array([24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72])
lin10 = np.array([21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95])
lin11 = np.array([78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92])
lin12 = np.array([16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57])
lin13 = np.array([86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58])
lin14 = np.array([19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40])
lin15 = np.array([4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66])
lin16 = np.array([88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69])
lin17 = np.array([4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36])
lin18 = np.array([20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16])
lin19 = np.array([20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54])
lin20 = np.array([1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48])

matriz = np.array([lin1,
                   lin2,
                   lin3,
                   lin4,
                   lin5,
                   lin6,
                   lin7,
                   lin8,
                   lin9,
                   lin10,
                   lin11,
                   lin12,
                   lin13,
                   lin14,
                   lin15,
                   lin16,
                   lin17,
                   lin18,
                   lin19,
                   lin20])
prod = 0  # Vari??vel atualizada sempre que um produto maior for encontrado
cont = 0  # Vari??vel atualizada quando um novo produto ?? calculado
el_prod = []  # Lista na qual ?? guardada os elementos geradores do maior produto

for i in range(20):  # Percorremos linhas e colunas, respectivamente
    for j in range(17):
        k = matriz[i][j] * matriz[i][j + 1] * matriz[i][j + 2] * matriz[i][j + 3]
        cont += 1
        if k > prod:
            prod = k
            el_prod = {f'{i}, {j}': matriz[i][j], f'{i}, {j + 1}': matriz[i][j + 1], f'{i}, {j + 2}':
                matriz[i][j + 2], f'{i}, {j + 3}': matriz[i][j + 3]}

for i in range(17):  # Percorremos diagonais de esquerda para direita
    for j in range(17):
        k = matriz[i][j] * matriz[i + 1][j + 1] * matriz[i + 2][j + 2] * matriz[i + 3][j + 3]
        cont += 1
        if k > prod:
            prod = k
            el_prod = {f'{i}, {j}': matriz[i][j], f'{i + 1}, {j + 1}': matriz[i + 1][j + 1], f'{i + 2}, {j + 2}':
                matriz[i + 2][j + 2], f'{i + 3}, {j + 3}': matriz[i + 3][j + 3]}

for i in range(3, 20):  # Percorremos diagonais de esquerda para direita
    for j in range(17):
        k = matriz[i][j] * matriz[i - 1][j + 1] * matriz[i - 2][j + 2] * matriz[i - 3][j + 3]
        cont += 1
        if k > prod:
            prod = k
            el_prod = {f'{i}, {j}': matriz[i][j], f'{i - 1}, {j + 1}': matriz[i - 1][j + 1], f'{i - 2}, {j + 2}':
                matriz[i - 2][j + 2], f'{i - 3}, {j + 3}': matriz[i - 3][j + 3]}

print(f'O maior produto ?? {prod}, resultado da multiplica????o de {el_prod}, sendo realizada {cont} opera????es')

