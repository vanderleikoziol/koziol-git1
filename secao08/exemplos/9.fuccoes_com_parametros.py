def quadrado_de_sete():
    return 7 * 7


print(quadrado_de_sete())

print('-='*40)

def quadrado(numero):
    return numero * numero


print(f'O quadrado é {quadrado(7)}')
print(f'O quadrado é {quadrado(2)}')
print(f'O quadrado é {quadrado(5)}')

print('-='*40)

def quadrado(numero):
    return numero * numero

ret = quadrado(6)
print(f'O quadrado é {ret}')

print('-='*40)

def quadrado(numero):
    return numero ** 2

ret = quadrado(6)
print(f'O quadrado é {ret}')

print('-='*40)

def cantar_parabens(aniversariante):
    print('Parabens para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva a {aniversariante}!')


for n in range(1):
    cantar_parabens('Marcela')
