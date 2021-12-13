"""
Leia um valor inteiro em segundos e imprima-o em horas, minutos e segundos.

"""

# Entrada


x = int(input('Informe o valor em segundos: '))

# Processamento


h = x // 3600
m = (x - (h * 3600)) // 60
s = (x - ((h * 3600) + (m * 60)))

# Saída


print(f'{h:.0f} H {m:.0f} MIN {s:.0f} SEG')
