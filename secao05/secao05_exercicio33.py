"""
Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço novo e
escreva uma mensagem em função do preço novo (de acordo com a segunda tabela).

 PREÇO ANTIGO           AUMENTO
Até R$ 50,00              5%
Entre R$ 50 e R$ 100      10%
Acima de R$ 100           15%


  PREÇO NOVO                      MENSAGEM
Até R$ 80,00                       Barato
Entre R$ 80 e R$ 120 inclusive     Normal
Entre R$ 120 e R$ 200 inclusive    Caro
Acima de R$ 200                    Muito Caro

"""


x = int(input('Informe o preço do produto: '))

if x < 50:
    preco = x * (1 + (5 / 100))
elif 50 <= x <= 100:
    preco = x * (1 + (10 / 100))
else:
    preco = x * (1 + (15 / 100))


if preco < 80:
    print(f'O novo preço é R$ {preco:.2f} e o valor está Barato.')
elif 80 <= preco <= 120:
    print(f'O novo preço é R$ {preco:.2f} e o valor está Normal.')
elif 120 <= preco <= 200:
    print(f'O novo preço é R$ {preco:.2f} e o valor está Caro.')
else:
    print(f'O novo preço é R$ {preco:.2f} e o valor está Muito Caro.')
