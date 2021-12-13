"""
Faça um programa que leia um número inteiro positivo de três digitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido.
Observações: Eu não consigo splitar um inteiro. Por isso antes eu preciso transformá-lo em string.

"""

# Entrada


n = int(input('Informe um número entre 100 e 999: '))

# Processamento


n = str(n)

# Saída


print(f'{n}')
print(n[::-1])
