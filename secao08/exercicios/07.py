c = int(input(f'Informe a temperatura em graus Celsius: '))


def converte_celsius_para_fahrenheit(c):
    return c * (9.0 / 5.0) + 32.0


print(f'A temperatura convertida em graus Fahrenheit é {converte_celsius_para_fahrenheit(c)} graus')
