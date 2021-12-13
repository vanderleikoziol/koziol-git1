"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:
- Estiver entre aspas simples -> 'uma string', '234', 'a', 'true', '42.3'
- sempre que estiver entre aspas duplas -> ""
- Estiver entre aspas simples triplas -> '''
- Estiver entre aspas duplas triplas -> (não colquei aqui em ra zão doerro)

Observações: 
a) nos casos de palavras como gina's bar, se eu quiser definir como string eu preciso
usar aspas duplas porque já há aspas simples na palavra.
b) se eu quiser escreve cada nome em uma linha eu preciso colocar \n na frente da palavra que quer quebrar a linha
exemplo: nome = "Angelina \nJolie".

Caracteres de escape: se eu abro uma string com aspas duplas eu preciso concluir com aspas duplas. Se por acoso eu
precisa usar aspas duplas no meio da palavra eu posso usar um carcter de escape conforme indicado a seguir.
nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

Para transformar em maiúscula:
print(nome.upper())
print(nome.lower())
print(nome.split()) -> Vai transformar em lista de strings=> ['Vanderlei', 'koziol'] neste caso criou duas lista.

[ 1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16
['V', 'a', 'n', 'd', 'e', 'r', 'l', 'e', 'i', '', 'K', 'o', 'z', 'i', 'o', 'l'] => Essa é a forma que o Python armazena.
nome = 'Vanderlei Koziol'
print(nome[0:10]) -> Vai imprimir Vanderlei => Slice de String
print(nome[11:17] -> Vai imprimir Koziol => Slice de string

Se eu der o comando print(nome.split()[0]) => vai transformar em:
     [P0          p1]
['Vanderlei', 'Koziol'] => uma lista, ou seja, duas listas separada por espaço.
Então, se:


print(nome.split[0]) => Vanderlei( a posição P0)
print(nome.split[1]) => Koziol ( a posição P1)

Ainda, caso eu queira escrever a string ao inverso.


print(nome[::-1]) => comece do primeiro elemento : e vá até o ultimo : e inverta -1

Para alterar o nome de uma string=> Substitua o V por W no nome do Vanderlei
print(nome.replace('V', 'W'))
 E para saber qual o tipo de variável =>
 print(type(nome))

 Texto Palindromo:

 texto = 'socorram me subino onibus em marrocos
 print(texto)
 print(texto[::-1])

 Ana também é uma palindromo


"""


nome = 'Vanderlei Koziol'
print(nome)
print(type(nome))

nome = "Gina's bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = """Angelina
Jolie"""
print(nome)
print(type(nome))


#Para transformar em maiúscula:


nome = 'Vanderlei Koziol'
print(nome.upper())
