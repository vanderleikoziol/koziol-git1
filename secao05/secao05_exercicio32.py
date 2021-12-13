"""
Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade. O programa
deve calcular o valor a ser pago por aquele lanche. Considere que a cada execução somente será calculado um pedido.
O cardápio da lanchonete segue o padrão abaixo:

"""


print()
print('               CARDÁPOIO')
print('_' * 40)
print(" ESPECIFICAÇÃO         CÓDIGO      PREÇO\nCachorro Quente          100        1.20\nBauru Simples            101"
      "        1.30\nBauru com Ovo            102        1.50\nHamburguer               103        1.20\nCheeseburguer"
      "            104        1.70\nSuco                     105        2.20\nRefrigerante             106        1.00")
print('_' * 40)


x = int(input('Informe o cógigo do produto escolhido: '))
y = int(input('Informe a quantidade de produtos: '))

if x == 100:
    valor = 1.2 * y
    print(f'O valor a pagar é R$ {valor:.2f}')
elif x == 101:
    valor = 1.3 * y
    print(f'O valor a pagar é R$ {valor:.2f}')
elif x == 102:
    valor = 1.5 * y
    print(f'O valor a pagar é R$ {valor:.2f}')
elif x == 103:
    valor = 1.2 * y
    print(f'O valor a pagar é R$ {valor:.2f}')
elif x == 104:
    valor = 1.7 * y
    print(f'O valor a pagar é R$ {valor:.2f}')
elif x == 105:
    valor = 2.2 * y
    print(f'O valor a pagar é R$ {valor:.2f}')
elif x == 106:
    valor = 1.0 * y
    print(f'O valor a pagar é R$ {valor:.2f}')
else:
    print('Produto não identificado.')

