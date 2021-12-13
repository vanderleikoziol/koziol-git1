"""
Faça um algorítimo que calcule a média ponderada das notas de três provas. A primeira e a segunda prova tem peso 1 e a
terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para
aprovação deve ser maior ou igual a 60 pontos.

"""
p1 = 1
p2 = 1
p3 = 2
sp = p1 + p2 + p3

n1 = int(input('Informe a primeira nota: '))
n2 = int(input('Informe a segunda nota: '))
n3 = int(input('Informe a terceira nota: '))

media = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / sp

if media > 60:
    print(f'Sua média foi {media:.0f} e você foi aprovado.')
else:
    print(f'Sua média foi {media:.0f} e você foi reprovado.')
