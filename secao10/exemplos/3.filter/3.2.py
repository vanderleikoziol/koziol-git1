import statistics

paises = ['', 'Argentina', '', 'Brasil', 'Chile', 'Colombia', '', '', 'Equador', '', 'Venezuela']

res = filter(None, paises)

print(list(res))

res = filter(lambda pais: len(pais) > 0, paises)

print(list(res))

res = filter(lambda pais: pais != '', paises)

print(list(res))
