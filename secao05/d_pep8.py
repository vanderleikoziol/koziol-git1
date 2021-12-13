"""
PEP8 - Python Enhancement Proposal
São Propostas de melhorias para a linguagem Python
The Zen of Python
import this
A ideia da PEP8 é que possamos escrever códigos de forma pythônica.

[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis.

def soma();
    pass

def soma_dois();

numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identação!


if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- Metodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Importes devem ser sempre feitos em linhas separadas;

# Errado
import sys, os

# import certo
import sys
import os
# não há problemas em utilizar:
from types import StringType, ListType

# caso tenha muistos importes de um mesmo pacote, recomenda-se fazer:
from types import (
    StringType
    ListType
    SetType
    OutroType
)

# Imports devem ser colocados no topo do arquivo depois de quaisquer comentários ou docstrings eantes
#de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções

# errado, não faça:
funcao( algo[ 1 ], { outro: 2 } )

# certo, deve ser feito
funcao(algo[1], {outro: 2})

# não faça

algo (1)

# faça:
algo(1)

#naõ faça:
dic [ 'chave'] = lista [indice]

# faça:

dic['chave'] = lista[indice]

#não faça:
 x              = 1
 y              = 2
 variavel_longa = 5

 #faça:
 x = 1
 y = 2
 variavel_longa = 5

 [7] - Termine sempre uma instrução com uma nova linha
"""
import this

