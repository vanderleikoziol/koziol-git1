"""
A tabela ASCII (American Standard Code for Information) é usada pela maior parte da industria de computadores
para a troca de informações.
Essa tabela codifica os caracteres para possibilitar o intercâmbio de informações na computação.
Um carcter é representado em memória através de um byte.
Um byte é o agrupamento de 8 bits
Bits é a representação binária 0 e 1.
Então 2 elevado a 8 tem-se 256 combinações possíveis.
Nessas 256 representações de caracteres divide-se em tres partes sendo:

Primeira parte: Posição 0 até a posição 31 => Têm-se os caracteres de controle como enter, esc, setas para cima,
para baixo, para esquerda, para direita.

Na parte central da tabela: Posição 32 até a posição 127 => Têm-se a tabela ASCII normal com a representação
dos caracteres:
1. Números da posição 48 até a 57
2. Alfabeto maiúsculo da posição 65 até a 90
3. Alfabeto minúsculo da posição 97 até a 122
4. Na última parte da tabela da posição 128 até 255 têm-se a tabela ASCII Estendida com os caracteres gráficos, os
caracteres acentuados, dentre outros.

Na linguagem de programação Python têm-se duas funções:

ord: retorna a ordem do caractere indicado
chr: retorna o caractere da ordem indicada
Exemplos:
Vamos criar um código fonte para percorrer a tabela de códigos ASC na sequência de todos os caracteres números.

nros = "" => aqui temos uma string comçando com valor nulo que vou juntar a cada passo da estrutura de repetição for
um caracter da tabela, ou seja, os caracteres números serão colados, juntados, concatenados para formar a sequência
de todos os caracteres números.

for i in range(48, 58): => implementar um range de 48 até 57 ( 57 porque é n-1)

nros = nros + chr(i) => na string números vamos concatenar o yes e um caractere da tabela ASCII. Então a função chr
retorna o caracter da tabela de códigos ASCII correspondente a posição de cada pelo argumento, que neste caso o valor
da variável i que vai de 47 até 57.

Vamos repertir a mesma operação para as letras maíúsculas e minúsculas.


"""

nros = ""
for i in range(48, 58):
    nros = nros + chr(i)


maius = minus = ""
for i in range(0, 26):
    maius = maius + chr(ord('A') + i)
    minus = minus + chr(ord('a') + i)

print(f'Números: {nros}')
print(f'Maiúsculas: {maius}')
print(f'Minúsculas: {minus}')
