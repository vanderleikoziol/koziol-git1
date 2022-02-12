import _statistics


usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': []},
]
print(usuarios)

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

print(inativos)

inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)