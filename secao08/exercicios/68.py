def intercala(str1, str2):
    """
    Vai receber duas palavras exemplo (cafe e preto). O vetor1 quando o y = 1 vai receber o vetor2 na posição x = 0 (P)
    quando o y for = 3 vai receber o vetor2 na posição 1 (R) e quando o y for = 5 vai receber o vetor2 na posição 2 (E)
    O exercício pede que a string intercalada retorne na primeira string, então a posição 3 e 4 (t, o) do vetor2 não
    é utilizada.
    :param str1: primeira palavra informada pelo usuário.
    :param str2: segunda palavra informada pelo usuário.
    :return: palavras intercaladas até o tamanho da primeira palavra.
    """
    vet1 = list(str1)
    vet2 = list(str2)
    t = len(vet1)
    x = 0
    y = 1
    for i in range(t):
        if x < len(vet2) and y < len(vet1):
            vet1.insert(y, vet2[x].upper())
            x += 1
            y += 2
    return vet1


a = input('Digite a primeira palavra: ')
b = input('Digite a segunda palavra: ')

print('Palavras intercaladas: ', intercala(a, b))
