"""
Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.

"""

# Entradas


v1 = int(input('Informe o primeiro valor: '))
v2 = int(input('Informe o segundo valor: '))
v3 = int(input('Informe o terceiro valor: '))

# Processamento


q1 = v1 ** 2
q2 = v2 ** 2
q3 = v3 ** 2

soma = q1 + q2 + q3

# Saída


print(f'A soma dos quadrados é: {soma}')
