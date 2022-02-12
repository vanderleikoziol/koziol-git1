try:
    geek()
except:
    print('Deu algum problema')

print('-=' * 30)
try:
    geek()
except NameError:
    print('Você está usando uma função inexistente')

    print('-=' * 30)
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

print('-=' * 30)
try:
    len(5)
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')

print('-=' * 30)
try:
    geek()
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')

print('-=' * 30)
try:
    print('Geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')

print('-=' * 30)


def pega_valor(dicionario, chave):
    return dicionario[chave]


dic = {'nome': "Geek"}
print(pega_valor(dic, "nome"))

print('-=' * 30)


def pega_valor(dicionario, chave):  # 25:40 min
    try:
        return dicionario[chave]
    except KeyError:
        return None


dic = {'nome': "Geek"}
print(pega_valor(dic, "game"))
