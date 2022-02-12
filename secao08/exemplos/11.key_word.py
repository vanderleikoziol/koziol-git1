def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))
