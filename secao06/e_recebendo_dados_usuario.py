"""

nome = input('Qual seu nome? ')
print(f'Seja bem-vindo(a) {nome}')
idade = int(input('Qual sua idade? '))
print(f'A {nome} tem {idade} anos')
print(f'A {nome} nasceu em {2021 - idade}')



Recebendo dados do usuário.
 O input é um recurso integrado da lingua gem que está dentro de builtins.
 Se eu executar o comando dir() via terminal dentro do guppe vai me mostrar as opções e dentre elas builtins.
 Se eu executar o comando dir(__builtins__) vai mostrar dentre outras opções o input.

 Observações: todo dado recebido via teclado é uma string.
 Em Pytho tudo o que estiver entre:
 - Aspas simples => 'Angelina Jolie'
 - Aspas duplas => "Angelina Jolie"
 - Aspas simples triplas => '''Angelina Jolie'''

"""
# Aspas duplas triplas => """Angelina Jolie"""

# Entrada de dados

#print("Qual seu nome? ")
#nome = input()

nome = input('Qual seu nome? ')

# print('Seja bem-vindo(a) %s' % nome) (modelo antigo)
# print('Seja bem-vindo(a) {0}' .format(nome)) (moderno)
# A seguir o print mais atual
print(f'Seja bem-vindo(a) {nome}')

#print("Qual sua idade? ")
#idade = input()

idade = int(input('Qual sua idade? ')) #como toda entrada do teclado é uma string neste caso o int é um cast para tratar essa iformação como um inteiro.


# Processamento

# Saída
# print('A %s tem %s anos' % (nome, idade)) (modelo antigo)
# print('A {0} tem {1} anos' .format(nome, idade)) (moderno)
# A seguir o print mais atual
# print(f'A {nome} tem {idade} anos') => como eu fiz o cast com int() para a entrada da idade agora eu posso usar o comando a seguir:
print(f'A {nome} tem {idade} anos')

"""
 # int(idade) => cast
 Caste é a conversão de um tipo de dado para outro.

"""
print(f'A {nome} nasceu em {2021 - idade}') # neste caso quero saber que ano nasceu.



