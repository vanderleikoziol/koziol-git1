"""
Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.

"""

# Entrada


lado = float(input('Informe a media do lado do quadrado: '))

# Processamento


altura = lado
base = lado
area = base * altura

# Saída


print(f'A área do quadrado é {area:.2f}')
