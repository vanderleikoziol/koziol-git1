import numpy as np
matriz = np.zeros([4, 4], int)
for linha in range(4):
    for coluna in range(4):
        matriz[linha][coluna] = linha * coluna
print(f'[{",".join(map(str,matriz[0]))}]\n[{",".join(map(str,matriz[1]))}]\n[{",".join(map(str,matriz[2]))}]\n'
      f'[{",".join(map(str,matriz[3]))}]')
