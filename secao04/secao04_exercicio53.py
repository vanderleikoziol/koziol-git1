"""
Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bem como preço do metro de tela p.
Imprima o custo para cercar este terreno com tela.

"""

# Entrada


c = int(input('Informe o comprimento do terreno: '))
l = int(input('Informe a largura do terreno: '))
p = int(input('Informe o preço do metro de tela: R$ '))


# Processamento


x = ((c + c) + (l + l)) * p

# Saída


print(f'O custo para cercar o terreno é R$ {x:.2f}.')
