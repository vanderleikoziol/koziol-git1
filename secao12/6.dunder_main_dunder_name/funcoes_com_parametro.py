def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))
    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(lista))
else:
    print('O módulo funções_com_parametro.py foi importado')
