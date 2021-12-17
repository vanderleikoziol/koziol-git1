"""
Tipo Float => números com casas decimais.
O separador de casas decimais em programação é sempre o ponto.

valor = 1,44 => errado (se eu executar print((type)valor) o Python vai entender como tupla.
valor = 1.44 => certo
Observações: se eu estiver no terminal e digitar print(valor) o valor da variável será impresso. Mas, se eu estiver
no console eu preciso informar
print((type)valor)
"""
# Observações:

valor = 1.44
print(valor)
print(type(valor))
# Eu posso trabalhar com dupla atribuição
#(neste caso estou declarando duas variáveis e passando o valor 1 para valor1 e,
#o valor 44 para valor2.
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))
# Todas as operações feitas com inteiro tambem podem ser feitas com ponto flutuante

#É possível converter um float para um inteiro mas perde-se precisão.
res = int(valor)
print(res)
print(type(res))
# Podemos trabalhar com números complexos
# o número complexo é representado por j.
# Exemplo 5j
5j
print(type(5j))
# vai resultar em 'complex'
# Se você que criar uma variável do tipo complexa basta adicionar o J nesta variável
variavel = 5j
"""
 5j
5j
>>> type(5j)
<class 'complex'>
>>> variavel = 5j
>>> type(variavel)
<class 'complex'>
>>> variavel ** 2
(-25+0j)

"""



