h = int(input(f'Informe a hora: '))
m = int(input(f'Informe os minutos: '))
s = int(input(f'Informe os segundos: '))


def converte_horas(h, m, s):
    return (h * 3600) + (m * 60) + s


print(f'O total de segundos é: {converte_horas(h, m, s)}')
