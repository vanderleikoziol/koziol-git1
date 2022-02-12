pontoV1 = {'x': 0, 'y': 0}
pontoV2 = {'x': 10, 'y': 10}

ponto = {'x': int(input('Digite o valor de x: ')), 'y': int(input('Digite o valor de y: '))}


def dentro_ret(ponto_v1, ponto_v2, ponto):
    if ponto_v1.get('x') < ponto.get('x') < ponto_v2.get('x') and \
            ponto_v1.get('y') < ponto.get('y') < ponto_v2.get('y'):
        return 1
    return 0


print()
print('Retangulo V1: x = 0, y = 0 | v2 x = 10, y = 10')
if dentro_ret(pontoV1, pontoV2, ponto) == 1:
    print('Ponto dentro do retângulo!')
else:
    print('Ponto fora do retângulo!')
