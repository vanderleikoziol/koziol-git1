"""
Dados n e dois números naturais positivos, i e j, diferentes de 0, imprimir em ordem crescente os n primeiros naturais
que são múltiplos de i ou de j e ou de ambos. Exemplo: Para n = 6, i = 2 e j = 3 a saída deverá ser: 0,2,3,4,6,8.

"""

n = int(input('Informe o valor de n: '))
i = int(input('Informe o valor de i: '))
j = int(input('Informe o valor de y: '))

multiplos = 0
contador = 0

while True:
    if multiplos % i == 0 or multiplos % j == 0:
        print(multiplos)
        contador += 1

    multiplos += 1
    if contador == n:
        break
