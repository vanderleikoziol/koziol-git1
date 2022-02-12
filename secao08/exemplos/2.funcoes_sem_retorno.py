def diz_oi():
    print('Oi!')


diz_oi()

print('-=' * 50)


def cantar_parabens():
    print('Parabens para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva a aniversariante!')


for n in range(5):
    cantar_parabens()

print('-=' * 50)

canta = cantar_parabens

canta()

