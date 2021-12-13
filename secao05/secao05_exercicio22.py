"""
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
As condições para aposentadoria são:
1 => Ter pelo menos 65 anos.
2 => Ou ter trabalhado pelo menos 30 anos.
3 => Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

"""

idade = int(input('Informe sua idade: '))
ts = int(input('Informe quantos anos você trabalhou: '))

var1 = idade >= 60 and ts >= 25
var2 = idade >= 65 or ts >= 30

if var1 or var2 == True:
    print('Pode aposentar')
else:
    print('Não tem direito a aposentadoria')