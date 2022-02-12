try:
    with open('University.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo.\n')
except FileExistsError:
    print('Arquivo já existe')
    