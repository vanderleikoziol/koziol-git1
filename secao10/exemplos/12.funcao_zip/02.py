prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

print('-='*30)

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
