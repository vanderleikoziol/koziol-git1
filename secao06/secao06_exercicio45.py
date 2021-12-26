"""
Faça um algorítimo que converta uma velocidade expressa em Km/h para m/s e vise versa. Você deve criar um menu com as
duas opções de conversão e com uma opção para finalizar o programa. O usuário poderá fazer quantas conversões desejar,
sendo que o programa só será finalizado quando a opção de finalizar for escolhida.

"""


while True:
    print('_' * 35)
    d = int(input('Informe o valor da distância: '))
    t = int(input('Informe o valor do tempo: '))
    print('_'*35)
    print('Digite 1 para converter Km/h em m/s.\nDigite 2 para converter m/s em km/h.\nDigite 3 para sair.')
    print('_' * 35)
    x = int(input('Informe a opção: '))
    if x == 1:
        y = (d * 1000) / (t * (60 * 60))
        print(f'A velocidade de {d} Km percorridos em {t} hora equivale a {y:.0f} metros percorridos por segundo.')
    elif x == 2:
        y = d * (t * 3.6)
        print(f'A velocidade de {d} metros percorridos em {t} segundos equivale a {y:.0f} Km percorridos por hora.')
    elif x == 3:
        break





