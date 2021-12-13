"""
Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.
A área do círculo é π * raio elevado ao qudrado.
Sendo π => 3.141592

"""

# Entradas


raio = float(input('Informe o valor do raio: '))

# Processamento


area = 3.141592 * (raio ** 2)

# Saída


print(f'A área do círculo é {area:.4f}.')
