"""
Uma empresa vende o mesmo produto para quatro estados diferente. Cada estado possui uma taxa diferente de imposto
sobre o produto:
MG => 7%
SP => 12%
RJ => 15%
MS = 8%
Faça um programa em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço final do
produto acrescido do imposto do estado que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem.

"""

valor = int(input('Informe o valor do produto: '))
uf = input('Informe o estado: ')

if uf.lower() == 'mg':
    preco = valor * (1 + (7 / 100))
    print(f'O preço do produto com imposto é {preco:.2f}.')
elif uf.lower() == 'sp':
    preco = valor * (1 + (12 / 100))
    print(f'O preço do produto com imposto é {preco:.2f}.')
elif uf.lower() == 'rj':
    preco = valor * (1 + (15 / 100))
    print(f'O preço do produto com imposto é {preco:.2f}.')
elif uf.lower() == 'ms':
    preco = valor * (1 + (8 / 100))
    print(f'O preço do produto com imposto é {preco:.2f}.')
else:
    print("Informe um estado válido.")
