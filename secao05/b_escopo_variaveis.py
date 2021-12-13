"""
Escopo de Variáveis

Escopo é a limitação de algo

/_____________________________________________/
     Esse é o escopo, ou tamanho, não vem antes nem depois. está dentro deste espaço.

Em escopo de variáveis precisamos entender qual a limitação desta variável. Aonde essa variável vai ser reconhecida
dentro do programa.
Quando falamos em variáveis há dois casos de escopo:

a) Escopo da variáveis globais => são reconheciodas, seu escopo compreende todo o programa.
b) Escopo das variáveis locais => são reconhecidas apenas no bloco onde foram declaradas. Seu escopo está limitado
ao bloco onde foi declarad.

Para declarar variáveis em Python fazemos nome_da_variavel = valor_da_variavel
Veja exemplo: 01

Observações: Python é uma libguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável nós não colocamos
o tipo de dados dela. Esse tipo é inferido ao atribuirmos o valor a ela.

Exemplo em c:
int numero = 42;
Exemplo em Java:
int numero = 42;
Reatribuição não é possível fazer em linguagem C e nem em Java. Veja exemplo 02

Observações importante.
Caso tente imprimir uma variável que não existe vai aparecer um erro erroName e informado que a variável não existe.
"""
# Exemplo 01: Primeiro exemplo (numero = nome da variável e 42 é o valor da variável)

numero = 42  #Esse é um exemplo de variável global
print(numero)
print(type(numero))
#neste caso reconheceu como número


#Observações: Reatribuição (variável número anteriormente era int e agora passa a ser string) Isso só pode ser feito
#em Python.

numero = 'koziol'
print(numero)
print(type(numero))
#neste caso reconheceu como string

# Exemplo02: Tipo de variável local.

numero = 2
if numero > 10:
    novo = numero + 10
    print(novo)

#essa variável novo que está dentro do bloco do if é uma variavel local que pertence a esse bloco apenas. Neste caso
#como a variável numero é menor que 10 a operação nem vai entrar no bloco para criar essa variável. E se concultada
# ela não vai aparecer. Uma das formar dessa variável aparecer era eu declarar como novo = 0 depois da declaraçãod da
#variavel numero.