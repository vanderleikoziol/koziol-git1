"""
Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor do kwh, e para cada habitante
 entre com os seguintes dados: Consumo mês e código do consumidor.
 1 - Residencial
 2 - Comercial
 3 - Industrial
No final imprima o maior, o menor e a média do consumo dos habitantes; e por fim o tatal do consumo de cada categoria
de consumidor.

"""
cod_residencial = 1
cod_comercial = 2
cod_industrial = 3

conta_residencial = 0
conta_comercial = 0
conta_industrial = 0

consumo_residencial = 0
consumo_comercial = 0
consumo_industrial = 0

maior = -999
menor = 999

while True:
    x = int(input('Informe o consumo em kwh: '))
    y = int(input('Informe o tipo de consumo: '))
    if y == 1:
        conta_residencial += 1
        consumo_residencial += x
        if x > 0:
            if x > maior:
                maior = x
            else:
                if x < menor:
                    menor = x
    elif y == 2:
        conta_comercial += 1
        consumo_comercial += x
        if x > 0:
            if x > maior:
                maior = x
            else:
                if x < menor:
                    menor = x
    elif y == 3:
        conta_industrial += 1
        consumo_industrial += x
        if x > 0:
            if x > maior:
                maior = x
            else:
                if x < menor:
                    menor = x
    else:
        break
total_habitantes = conta_residencial + conta_comercial + conta_industrial
total_consumo = consumo_residencial + consumo_comercial + consumo_industrial
media_habitantes = total_consumo / total_habitantes

print('-'*40)
print(f'O maior valor => {maior}\nO menor valor => {menor}')
print(f'Media consumo por habitantes => {media_habitantes:.2f}')
print(f'Total de consumo residêncial => {consumo_residencial}')
print(f'Total de consumo comercial => {consumo_comercial}')
print(f'Total de consumo Industrial => {consumo_industrial}')





