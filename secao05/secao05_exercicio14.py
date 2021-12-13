"""
A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 a 10, respctivamente
a um trabalho de laboratório (tl), a uma avaliação semestral (avs) e a um exame final (ef). A média das três notas mencionadas
anteriormente obedece aos pesos:
Trabalho de laboratório: 2
Avaliação semestral: 3
Exame final: 5
De acordo com o resultado, mostre na tela:
Reprovado => média entre 0 e 2.9
Recuperação => média entre 3 e 4.9
Aprovado => superior a 4.9

"""
tl = float(input('Informe a nota do trabalho de laboratório: '))
avs = float(input('Informe a nota da avaliação semestral: '))
ef = float(input('Informe a nota do exame final: '))

ptl = 2
pavs = 3
pef = 5
sp = ptl + avs + pef

media = ((tl * ptl) + (avs * pavs) + (ef * pef)) / sp

if media <= 2.9:
    print(f'Sua média foi {media:.2f} e você foi reprovado.')
elif 2.9 < media <= 4.9:
    print(f'Sua média foi {media:.2f} e você está em recuperação.')
else:
    print(f'Sua média foi {media:.2f} e você foi aprovado.')
