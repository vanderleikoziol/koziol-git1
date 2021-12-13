"""
Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância em km da origem:
a) (0.0)
b)(-3.-1)

"""

# Entradas


x = int(input('Informe o valor da coordenada x: '))
y = int(input('Informe o valor da coordenada y: '))

# Processamento


d1 = (((x - (- 3)) ** 2) + ((y - (- 1)) ** 2)) ** (1/2)
d2 = (((x - 0) ** 2) + ((y - 0) ** 2)) ** (1/2)


# Saída


print(f'A distância é {d1:.2f} km')
print(f'A distância é {d2:.2f} km')
