"""
Funções com retorno
"""
numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f'Retorno de pop()=> {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print() => {ret_pr}')

print('-=' * 50)


def quadrado_de_7():
    print(7 * 7)


ret = quadrado_de_7()

print(f'Retorno de ret => {ret}')

print('-=' * 50)


def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()

print(f'Retorno de ret => {ret}')

print('-=' * 50)


def quadrado_de_7():
    return 7 * 7

print(f'Retorno da funçõa=> {quadrado_de_7()}')

print('-=' * 50)

def diz_oi():
    return ('Oi ')

alguem = 'Pedro!'

print(diz_oi() + alguem)

print('-=' * 50)

def diz_oi():
    return 'Oi '
    print('Estou sendo executado após o retorno...')


print(diz_oi())
