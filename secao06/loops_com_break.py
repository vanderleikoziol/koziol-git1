"""
Saindo de loops com break.
Utilizamos o braek para sair de loops de maneira projetada.

Exemplo 1 com for

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop')
Neste caso estamos dando o comando para que se o número for 6 o loop pare.


Exemplo 2 com while

while True:
    comando = input('Digite sair para sair: ')
    if comando == 'sair':
        break

Neste caso estou forçando um loop infinito. Pois o while sempre vai ser True. Então, enquanto não for digitado sair
o loop continuará rodando.

"""

print('Exemplo 1')

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop')


print('Exemplo 1')

while True:
    comando = input('Digite sair para sair: ')
    if comando == 'sair':
        break
