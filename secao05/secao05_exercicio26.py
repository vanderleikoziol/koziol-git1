"""
Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em
km/l e escreva uma mensagem de acordo com a tabela abaixo:
1. => Consumo menor que 8 km/l o carro deve ser vendido.
2. => Consumo entre 8 e 14 km/l o carro é econômico.
3. => Consumo maior que 12 km/l o carro é super econômico.

"""
litros = float(input('Informe o consumo de combustível em litros: '))
km = float(input('Informe a distância percorrida em KM: '))
preco_litro = float(input('Informe o valor do litro de combustível em R$: '))


consumo = km / litros
custo = litros * preco_litro
valor_km = consumo / preco_litro


print(f'O valor gasto para abastecer foi R$ {custo:.2f}.')

if consumo < 8:
    print(f'O consumo do carro é de {consumo} km/l. Venda o carro!')
elif 8 < consumo < 12:
    print(f'O consumo do carro é de {consumo} km/l. Econômico!')
else:
    print(f'O consumo do carro é de {consumo} km/l. Super econômico!')

print(f'O valor do KM rodado é R$: {valor_km:.2f}.')

orc = float(input('Informe a distância da viagem em KM: '))


orcamento = orc / valor_km

print(f'O valor da viagem é: R$ {orcamento:.2f}.')
