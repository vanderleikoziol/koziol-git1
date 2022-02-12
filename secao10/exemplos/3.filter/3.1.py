import statistics

valores = 1,  2, 3, 4, 5, 6

media = (sum(valores) / len(valores))

print(media)

print('-='*30)

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

media = statistics.mean(dados)

print(f'A média é => {media}')

res = filter(lambda x: x > media, dados)

print(f'1⁰ Print => Os valores maiores que a media {media:.2f} são => {list(res)}')

print(f'2⁰ Print => Os valores maiores que a media {media:.2f} são => {list(res)}')
