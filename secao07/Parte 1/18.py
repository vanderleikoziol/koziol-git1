numeros = []

for n in range(10):
    valor = int(input(f'Informe o valor {n + 1}/10: '))
    numeros.append(valor)

x = int(input('Informe um valor para encontrar os múltiplos: '))
contador = 0

for valor in numeros:
    if valor % x == 0:
        print(f'O valor {valor} é múltiplo de {x}')
        contador += 1

print(f'Temos {contador} números múltimos de {x} no vetor {numeros}')