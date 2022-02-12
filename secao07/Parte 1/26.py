"""
1. Criar o vetor.
2. Encontrar a média (m) do vetor (y).
3. Encontrar o desvio entre cada valor do vetor e a média em módulo, para que seja positivo. d = (m - y) ou (y - m)
e fazer a média do quadrado de cada desvio para encontrar a variância. v = d **2 / média do desvio
4. Encontrar o desvio padrão. dp = raiz quadrada de v

"""
from math import sqrt

t = 5
vetor = []
desvio = []
n = 0

# 1. Criação do vetor
for i in range(t):
    vetor.append(int(input(f'Informe o valor de {i + 1}/{t}:')))

# 2. Encontrar a média do vetor
media = sum(vetor) / len(vetor)

# 3. Encontrar o desvio de cada valor do vetor
for i in vetor:
    if i - media > 0:
        y = (i - media) ** 2
        desvio.append(y)
    else:
        y = (media - i) ** 2
        desvio.append(y)
variancia = sum(desvio) / len(desvio)

desvio_padrao = sqrt(variancia)

print(f'A variancia é {variancia} e o desvio padrão é {desvio_padrao:.4f}.')
