"""
O loop while serve para iterar sobre sequências.
A grande diferença é que a forma geral de um loop while é diferente.

while expressão_boleana:
    //execução do loop
Obs. Tudo o que estiver dentro do bloco do while vai ser repetida enquanto essa condição boleana for verdadeira.

A expressão Booleana é qualquer expressão cujo resultado seja verdadeiro ou falso.
Exemplo de Booleana

num = 5

num <= 5
True

num > 10
False
***************************************************************************************************
Exemplo de código.

numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1
Leitura=>
Linha 1 => Criei uma variável número inicializada em 1
Linha 2 => Criado o bloco do while que deverá ser executado enquanto o número for menor do que 10.
Linha 3 => Verifica se o número é menor que 10 e imprime o número.
Linha 4 => Esse número vai ser incrementado e receber + 1.

**********************************************************************************************************
Em um loop while é importante observar o critério de parada para não causar um loop infinito.
**********************************************************************************************************
Veja o código a seguir:
numero = 1
while numero < 10:
    print(numero)
Neste caso o número é igual a 1 e o while está informando que enquanto for menor que 10 é para imprimir. Isso é um
loop infinito.

"""

print('Exemplo 1')
numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1
print('Exemplo 2')
resposta = ''
while resposta != 'n':
    resposta = input('Informe n para parar: ')
