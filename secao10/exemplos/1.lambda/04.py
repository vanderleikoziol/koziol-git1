autores = ['Machado de Assis', 'Ruy Barbosa', 'Cabral C. Neto', 'Marcos Silva', 'Ernandes Azevedo', 'Paulo Freire',
           'Fernando Pessoa', 'Milton Farias Braga', 'Helio F. Couto', 'A. P. Garcia']
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
