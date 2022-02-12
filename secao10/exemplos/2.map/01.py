import math

def area(r):
    """calcula a área de um circulo com raio r"""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

print('-='*30)

raios = [2, 5, 7.1, 0.3, 10, 44]

areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

print('-='*30)

print(list(map(lambda r: math.pi * (r ** 2), raios)))
