print(all([0, 1, 2, 3, 4]))
print(all([1, 2, 3, 4]))

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))  # min 16:42


print(any([0, 1, 2, 3, 4]))

print(any([0, False, {}, ()]))  # 20:31min

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))  # 21:25 min
