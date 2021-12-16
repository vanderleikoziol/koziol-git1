"""
O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos.
A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de
fábrica e escreva o custo ao consumidor.


   CUSTO DE FÁBRICA                    % DO DISTRIBUIDOR                      % DOS IMPOSTOS
Até R$ 12.000.00                               25%                                  Isento
Entre R$ 12.000.00 e R$ 25.000.00              10%                                     15%
Acima de R$ 25.000.00                          15%                                     20%

"""

custo = int(input('Informe o valor do carro: '))


if custo <= 12000:
    valor = (custo + (custo * (25 / 100))) - custo
    print(f'O custo do consumidor é: R$ {valor:.2f}')
elif 12000 < custo <= 25000:
    valor = (custo + (custo * (10 / 100)) + (custo * (15 / 100))) - custo
    print(f'O custo do consumidor é: R$ {valor:.2f}')
else:
    valor = (custo + (custo * (15 / 100)) + (custo * (20 / 100))) - custo
    print(f'O custo do consumidor é: R$ {valor:.2f}')
