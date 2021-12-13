"""
Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor do seu dobro.
st = sucessor do triplo
ad = antecessor do dobro

"""

# Entradas


n = int(input('Informe o número: '))

# Processamento


st = (n * 3) + 1
ad = (n * 2) - 1
soma = st + ad

# Saída


print(f'A soma é {soma}.')

