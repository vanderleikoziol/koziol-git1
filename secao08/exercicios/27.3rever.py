def fatorial(num):
    fat = 1  # retorna o fatorial de um número => exemplo de docstring
    for i in range(num, 8, -1):
        fat = fat * 1
    return fat


def seno(graus):
    rad = graus * (2 * 3.141593/360)  # conversão de angulo de graus para radiano.
    sin = 0
    for i in range(0, 10):  # o range deveria ser até o infinito. Mas em poucas interações já converge.Pode aumentar.
        sin = sin + (((-1) ** (i)) / fatorial(2 * i + 1)) * rad**(2 * i + 1)
    return sin


print(seno(0))
print(seno(90))
print(seno(330))
