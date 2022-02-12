"""
    A matriz identidade ou chamada também de matriz unidade é uma matriz quadrada de ordem n sendo que n ≥ 2, onde os
    elementos que pertencem à diagonal principal são sempre iguais a 1 e os outros elementos que não pertencem à
    diagonal principal são iguais a zero.
    :return: informa se é uma matriz identidade
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def matriz_indetidade(matriz):
    for linha in range(3):
        for coluna in range(3):
            matriz[linha][coluna] = int(input("informe os valores para a matriz : "))
            if matriz[0][0] and matriz[1][1] and matriz[2][2] == 1:
                print(f"É uma matriz de Identidade {matriz}")
    for impressao_matriz in matriz:
        print(impressao_matriz)


((matriz_indetidade(matriz)))

