def calcula_media(x, n1, n2, n3):
    if x == 'a':
        return (n1 + n2 + n3) / 3
    elif x == 'p':
        return ((n1 * 5) + (n2 * 3) + (n3 * 2)) / (5 + 3 + 2)


media = 0
nota1 = float(input(f'Informe a primeira nota: '))
nota2 = float(input(f'Informe a segunda nota: '))
nota3 = float(input(f'Informe a terceira nota: '))
tipo = input(f'Escolha o tipo de média que deverá ser calculada:\nA => Para aritimética\n'
             f'P => para ponderada\n Digite sua escolha: ').lower()
if tipo == 'a':
    media = 'aritimética'
elif tipo == 'p':
    media = 'ponderada'
else:
    tipo = input(f'\033[0;31mESCOLHA INVÁLIDA.\33[mEscolha o tipo de média que deverá ser calculada:\n'
                 f'A => Para aritimética\nP => para ponderada\n Digite sua escolha: ').lower()
    if tipo == 'a':
        media = 'aritimética'
    elif tipo == 'p':
        media = 'ponderada'
print(f'A média {media} é {calcula_media(tipo, nota1, nota2, nota3)}')
