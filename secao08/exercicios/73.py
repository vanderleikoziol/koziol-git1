def pesquisa(sexo, cor_olhos, cor_cabelos, idade):
    """
    Esta função retorna uma dicionário com chave e valor que será usado para a entrada de dados.
    :param sexo:
    :param cor_olhos:
    :param cor_cabelos:
    :param idade:
    :return:
    """
    return {'sexo': sexo, 'cor_olhos': cor_olhos, 'cor_cabelos': cor_cabelos, 'idade': idade}


def entrada_dados():
    """
    Esta é a função de entrada de valor que faz um for no range(n⁰ de entradas de dados que eu quero) cuja variável de
    input é a mesma da função pesquisa. Ao final o vetPesquisa[] declarado nesta função append pesquisa, ou seja,
    o dicionário com chave e valor, cujos valores passam a ser os inputs desta função.
    :keyword parâmetros da função pesquisa
    :return: o vetor pesquisa com as informações inseridas pelo usuário.
    """
    vetPesquisa = []
    for i in range(5):
        print()
        print(f'{(i + 1)}º')

        sexo = input('Digite o Sexo F ou M: ')
        while sexo.upper() != 'F' and sexo.upper() != 'M':
            sexo = input('Digite o Sexo usando somente uma letra F ou M: ')

        cor_olhos = input('Digite dos olhos A - Azuis ou C - Castanhos: ')
        while cor_olhos.upper() != 'A' and cor_olhos.upper() != 'C':
            cor_olhos = input('Digite a cor dos olhos usando somente uma letra A - Azuis ou C - Castanhos: ')

        cor_cabelos = input('Digite a cor dos cabelos L - Louros, P - Pretos, C - Castanhos: ')
        while cor_cabelos.upper() != 'L' and cor_cabelos.upper() != 'P' and cor_cabelos.upper() != 'C':
            cor_cabelos = input(
                'Digite a cor dos cabelos usando somente uma letra L - Louros, P - Pretos, C - Castanhos: ')

        idade = int(input('Digite a idade: '))

        vetPesquisa.append(pesquisa(sexo, cor_olhos, cor_cabelos, idade))

    return vetPesquisa


def media_idade(vet_pesquisa, olhos, cabelos):
    """
    Vai procurar no vet_pesquisa na posição i se cor de olhos e cor de cabelos são iguais e calcular média idade.
    Verifica a condição chave = cor dos olhos e a posição i a chave for igual ao parâmetro para olhos e cabelos.
    :param vet_pesquisa: retorno da função entrada de dados
    :param olhos: informado pelo usuário
    :param cabelos: informado pelo usuário
    :return: média de idade
    """
    media_idade = 0
    count = 0
    for i in range(len(vet_pesquisa)):
        for chave in vet_pesquisa[i]:
            if chave == 'cor_olhos' and \
                    (vet_pesquisa[i][chave].upper() == olhos.upper() and vet_pesquisa[i][
                        'cor_cabelos'].upper() == cabelos.upper()):
                count += 1
                media_idade += vetPesquisa[i]['idade']

    if count > 0:
        return (media_idade / count)
    return 0


print()


def maior_idade(vet_pesquisa):
    """
    Separo todas as idades em um vetor de idades e procuro a maior idade.
    :param vet_pesquisa: retorno da função entrada de dados
    :return: maior idade
    """
    vet_idade = []
    for i in range(len(vet_pesquisa)):
        for chave in vet_pesquisa[i]:
            if chave == 'idade':
                vet_idade.append(vet_pesquisa[i][chave])
    return max(vet_idade)


def qtd_feminino(vet_pesquisa, olhos, cabelos, idade1, idade2):
    """
    Fa uma condição se dentro do for para os parâmetros da função e o resultado através de um cont
    :param vet_pesquisa: retorno da função entrada de dados
    :param olhos: Informado pelo usuário
    :param cabelos: Informado pelo usuário
    :param idade1: Informado pelo usuário
    :param idade2: Informado pelo usuário
    :return: quantidade de pessoas que atende ao parâmetro
    """
    count = 0
    for i in range(len(vet_pesquisa)):
        for chave in vet_pesquisa[i]:
            if chave == 'cor_olhos' and \
                    (vet_pesquisa[i][chave].upper() == olhos.upper() and \
                     vet_pesquisa[i]['cor_cabelos'].upper() == cabelos.upper()) and \
                    (vet_pesquisa[i]['idade'] >= idade1 and vet_pesquisa[i]['idade'] <= idade2):
                count += 1

    return count


# Leitura dos dados
vetPesquisa = entrada_dados()

print()

# Média de idade das pessoas com olhos castanhos e cabelos pretos
print('Média de idade das pessoas com olhos castanhos e cabelos pretos: ', media_idade(vetPesquisa, 'c', 'p'))
print()

# Maior idade entre os habitantes
print('Maior idade entre os habitantes: ', maior_idade(vetPesquisa))
print()

# Quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35
print('Quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35: ',
      qtd_feminino(vetPesquisa, 'a', 'l', 18, 35))


