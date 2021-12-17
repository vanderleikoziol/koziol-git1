"""
Estruturas de repetição

Loop => Utilizamos o  for ou o while para iterar sobre sequências ou sobre valores iteráveis.
Exemplo de valores iteráveis:
String:
nome = Geek University
Lista:
lista = [1, 3, 5, 7, 9]
range:
numeros = range(1, 10) (uma range precisa ser transformado em lista)
for item in interavel:
    // execuçao do loop

Observações: o que estiver dentro da estrutura do for, ou seja, quatro espaços será executado e o que estiver na mesma
linha do for não será executado.

Exemplo de for:
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)
******************************************
1. Iterando sobre uma string
******************************************
for letra in nome:
    print(letra)
Leitura => para cada letra dentro deste interavel imprima letra.
*********************************************************
2. Iterando sobre uma lista
*********************************************************
for numero in lista:
print(numero)
Leitura => para cada numero na lista imprima esse numero.
*********************************************************
2. Iterando sobre um range
*********************************************************
for numero in range(1, 10):
    print(numero)
Leitura => para cada numero no range foi impresso o número  dentro do conceito n-1. O valor final não é inclusive.

************************************************************
COMO DESCOBRIR QUAL É O INDICE DE UMA LETRA
************************************************************
No caso de Geek University e quero descobrir qual o indice da letra v.
Observações: se for em Python Console e:
nome = 'Geek University'
valores = enumerate(nome)
Vai retornar um objeto do tipo enumerate.
help(enumerate)
Vai mostrar que é um objeto do tipo enumerate.
O que significa isso?
O enumerate vai criar um tupla.
exemplo:
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ''), (5, 'u'), ... até o final da palavra.

O enumerate coloca um indice para cada sequência da palavra.

----------------------------------------------------------------------------------------------
for indice, letra in enumerate(nome):
    print(nome[i])
Leitura => Para i de indice e v de valor dentro de enumerate nome imprima nome nesse indice.
É o mesmo que falar imprime nome na posição zero, na posição um, etc.

O comando a seguir retorna a mesma coisa:

for indice, letra in enumerate(nome):
    print(letra)

Para saber o valor:
for valor in enumerate(nome):
    print(valor)
-----------------------------------------------------------------------------------------------
OBSERVAÇÕES IMPORTANTES:
Se eu tenho dois valores e não preciso mostrar um deles basta eu usar o _. Veja exemplo a seguir:
for _, letra in enumerate(nome)
    print(letra)
Obs. Neste caso eu não tenho interesse no indice, então vou imprimir somente a letra.
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Se eu quero imprimir tudo na mesma linha:
for valor in enumerate(nome):
    print(valor, end='')
Obs. Se eu apertar o ctrl e clicar sobre a print eu também consigo acessar informação dada pelo Help.
-----------------------------------------------------------------------------------------------
NOVA FORMA DE UTILIZAR O FOR
-----------------------------------------------------------------------------------------------
qtd = int(input('Quantas vezes esse loop deve rodar: '))
for n in range(1, qtd):
    print(f'Imprimindo {n}')
Leitura=> Estou recebendo dados do usuário começando em 1 e indo até a quantidade informada pelo usuário e vou
imprimir o n.
Observações: O final do range não é inclusive. Se você quer executar completo deve colocar +1.
qtd = int(input('Quantas vezes esse loop deve rodar: '))
for n in range(1, qtd+1):
    print(f'Imprimindo {n}')
------------------------------------------------------------------------------------------------
CRIANDO UMA VARIÁVEL PARA UTILIZAR O FOR

qtd = int(input('Quantas vezes esse loop deve rodar: '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

Leitura =>
linha 1 => Estamos perguntando para o usuário quantas vezes o looping deve rodar.
Linha 2 => Criamos uma variável iniciada em zero para fazermos a soma dos valores indicados pelo usuário.
Linha 3 => Estamos fazendo um for iniciando em 1 e indo até a quantidade + 1.
Linha 4 => Estamos recebendo o número informado pelo usuário.
Linha 5 => Vamos somar o valor de soma mais o número
Linha 6 => No final quando sair do for vamos imprimir a soma.

**********************************************************************************************************
CONCATENIZAÇÃO DE STRING
**********************************************************************************************************

nome = 'Geek'
nome + 'University'
resulta em: 'Geek University'
nome * 30 = 'GeekGeekGeek' => você pode miltiplicar string.

"""
print('*'*20)
print('EXEMPLOS DE FOR')
print('*'*20)
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)
print('Iterando em uma string')
for letra in nome:
    print(letra)
print('*'*20)
print('Iterando em uma lista')
for numero in lista:
    print(numero)
print('*'*20)
print('Iterando em um range')
for numero in range(1, 10):
    print(numero)
print('*'*20)
print('Usando o iterate')
print('Primeira forma')
for indice, letra in enumerate(nome):
    print(nome[indice])
print('Segunda forma')
for indice, letra in enumerate(nome):
    print(letra)
print('Terceira forma')
for _, letra in enumerate(nome):
    print(letra)
print('Para saber o indice de cada letra')
for valor in enumerate(nome):
    print(valor)
print('Para saber somente o indice')
for valor in enumerate(nome):
    print(valor[0])
print('Para escrever tudo na mesma linha')
for valor in enumerate(nome):
    print(valor, end='')

print('*'*20)
print('Nova utilização do for')
qtd = int(input('Quantas vezes esse loop deve rodar: '))
for n in range(1, qtd):
    print(f'Imprimindo {n}')
print('Colocar + 1 para executar completo')
qtd = int(input('Quantas vezes esse loop deve rodar: '))
for n in range(1, qtd + 1):
    print(f'Imprimindo {n}')
print('*'*20)
print('criando uma variavél para usar a função for')
qtd = int(input('Quantas vezes esse loop deve rodar: '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')




