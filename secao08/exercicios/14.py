def calcula_custo(distancia, litros):
    if distancia / litros <= 8:
        return 'Venda o carro!'
    elif 8 < (distancia / litros) <= 12:
        return 'Econômico!'
    return 'Super econômico!'


x = int(input(f"Informe a quilometragem rodada: "))
y = int(input(f"Informe o n⁰ de litros de combustível gasto: "))
print(calcula_custo(x, y))
