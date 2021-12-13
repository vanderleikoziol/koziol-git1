"""
Faça um programa que leia o horário (hora, minuto e segundo) de início e a duração em segundos, de uma experiência
biológica. O programa deve resultar com o novo horário (hora, minuto e segundo) do termino da experiência.
Algorítimo

Entradas
Receber o tempo da experiência em segundos
Identificar a hora atual

Processamento
Identificar a hora atual
Transformar a hora atual em segundos
Somar o tempo da experiência em segundos
Transformar segundos em horas , minutos e segundos.

Saída
Imprimir o início da experiência em horas, minutos e segundos.
Imprimir a duração da experiência em horas, minutos e segundos.
Imprimir a hora do fim da experiência em horas minutos e segundos.

"""
from datetime import datetime

# Entrada


x = int(input('Informe o tempo da experiência em segundos: '))

# Processamento


horaagora = datetime.now()
hora = horaagora.hour
minuto = horaagora.minute
segundo = horaagora.second
sh = hora * 60 * 60
sm = minuto * 60
ts = x + segundo + sm + sh

h = x // 3600
m = (x - (h * 3600)) // 60
s = (x - ((h * 3600) + (m * 60)))

ht = ts // 3600
mt = (ts - (ht * 3600)) // 60
st = (ts - ((ht * 3600) + (mt * 60)))

# Saída


print(f'A experiência iniciou as: {hora}H {minuto}M {segundo}S')
print(f'O tempo de duração da experiência é de {h}H {m}M {s}S')
print(f'A experiência deverá encerrar às {ht}H {mt}M {st}S')



