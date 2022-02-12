def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}


print(mostra_nomes(**nomes))


print(f'resultado do exemplo 2')
def soma_numeros(a, b, c):
    print(a + b + c)


soma_numeros(1, 2, 3)

print(f'resultado do exemplo 2.1')
def soma_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_numeros(*lista)
soma_numeros(*tupla)
soma_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_numeros(**dicionario)

dicionario = dict(a=1, b=2, c=3, nome='Geek')
soma_numeros(**dicionario, lang='Python')
