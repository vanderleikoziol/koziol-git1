def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O {texto} será impresso na {cor}')


colore('Geek', 'Azul')

colore('Geek', '18')



print('-='*30)
def colore(texto, cor):
    cores = ('Verde', 'Amarelo', 'Azul', 'Branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError(f'Cor precisa estar entre:{cores}')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O {texto} será impresso na {cor}')


colore('Geek University', 'Verde')
colore('Geek University', 'Preto')

