def exponencial(numero, potencia):
    return numero ** potencia


print(exponencial(2, 3))
print(exponencial(3, 2))



print('-='*30)

def exponencial(numero=4, potencia=2):
    return numero ** potencia


print(exponencial(3))
print(exponencial(3, 5))
print(exponencial())


print('-='*30)

def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))
#print(soma(4))
#print(soma())
print('-='*30)

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Ozzy'))
