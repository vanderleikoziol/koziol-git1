
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

# com generators faz se assim

print(any(nome[0] == 'C' for nome in nomes))

# executando como list comprehension

res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# executando como generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)
