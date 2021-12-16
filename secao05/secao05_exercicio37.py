"""
As tarifas de certo parque de estacinonamento são as seguintes:
a) 1 e 2 horas => R$ 1.0 cada.
b) 3 e 4 horas => R$ 1.4 cada.
c) 5 Horas e seguintes => R$ 2.0 cada.
O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, que estacionar durante 61 minutos
pagará por duas horas que é o mesmo que pagaria se tivesse permanecido por 120 minutos. Os momentos de chegada e partida
são apresentados na forma de pares de inteiros, representado por horas e minutos.
Por exemplo, o par 12 50 representará dez para uma da tarde. Pretende-se criar um programa que, lidos pelo teclado os
momentos de chegada e de partida, escreva na tela o preço cobrado pelo estacionamento. Admite-se que chegadas e partidas
se dão com um intervalo de 24 horas. Portanto, se uma dada hora de chegada for superior à da partida, isso não é uma
situação de erro, antes siguinifica que a partida ocorreu no dia seguinte ao da chegada.

Etapas:
1. Receber a entrada em formato de lista e splitar.
*** usada a lista para receber os dois int, a função map para ler a lista e o split para separar.
2. Certificar que o usuário não vai lançar hora errada na entrada e na saída.
*** como não existe 24hs e inclusive 60 minutos na contagem, foi usada a fórmula -23 e -59 verificar o input.
3. Montar uma estrutura de repetição para retornar caso digite hora errada.
4. Calcular o tempo Total.
*** Transformar minutos em horas e dar parâmetros para entrar na condição if.
Se eu chego as 10h20min => hora_chegada => (10+(20/60)) = 10,33
Se eu saio as 11h40min => hora_saída => (11+(40/60) = 11,63
Tempo total => (11,63 - 10,33) = 1,33
5. Verificar se o carro não ficou de um dia para o outro.
*** A seguir, se a hora de chegada for maior ou igual a hora de saída é porque o carro ficou de um dia para outro.
Então 24hs do dia menos a hora de chegada vai me dar o número de horas do dia anterior e ai vou somar as horas
do dia atual.
6. Validar a condição de int do tempo total.
*** A condição if a seguir serve para atender o rquisito de hora inteira do programa. Se o inteiro do tempo total for
arredondado para baixo, o que é esse caso de 23.33333333333 ao somar 1 ele passa a ser 24. Caso contrário o tempo_total
será o inteiro do tempo_total.
7. Calcular o custo total
Primeiro vou declarar a variável custo_total = 0
Menor ou igual a 2 horas cobra R$ 1 por hora.
Considerando que a condição <= a 2 já foi atendida, então se for menor ou igual a 4, 2 hs já ocorreu
então no elif eu considero R$ 2,00 + (tempo_total -2) das duas hora que já considerei o custo e multiplico por R$ 1,4
(se o tempo total for 3 (2 + (3 - 2)) = 4 * 1,4 = custo
No else eu já tenho o custo de R$ 4,80 referente ( R$ 2,00 das duas primeira horas + R$ 1,40 da terceira e R$ 1,40 da
quarta hora)
Então eu considero o R$ 4,80 + (tempo total - as quatro hora que já considerei o custo) e multiplico por R$ 2,00
"""


chegada = list(map(int, input('Informe a hora de chegada, ex: 10 50 =>: ').split()))

while chegada[0] * (chegada[0] - 23) > 0 or chegada[1] * (chegada[1] - 59) > 0:
    print('Hora inválida')
    chegada = list(map(int, input('Informe a hora de chegada, ex: 10 50 =>: ').split()))

saida = list(map(int, input('Informe a hora de saída, ex: 11 50 =>: ').split()))

while saida[0] * (saida[0] - 23) > 0 or saida[1] * (saida[1] - 59) > 0:
    print('Hora inválida')
    saida = list(map(int, input('Informe a hora da saída, ex: 11 50 =>: ').split()))

hora_chegada = chegada[0] + (chegada[1] / 60)
hora_saida = saida[0] + (saida[1] / 60)
tempo_total = hora_saida - hora_chegada


if hora_chegada >= hora_saida:
    tempo_total = (24 - hora_chegada) + hora_saida

if int(tempo_total) < tempo_total:
    tempo_total = int(tempo_total) + 1

else:
    tempo_total = int(tempo_total)

print(f'O carro permaneceu no estacionamento por: {tempo_total:.2f} horas')

custo_total = 0

if tempo_total <= 2:
    custo_total = tempo_total * 1
elif tempo_total <= 4:
    custo_total = 2 + (tempo_total - 2) * 1.4
else:
    custo_total = (2 + 2.8) + ((tempo_total - 4) * 2)
    print(f'O valor a pagar é de: R$ {custo_total:.2f}')
