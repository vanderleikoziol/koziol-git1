"""
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequência arbitrária de notas
(válidas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente média aritmétrica. O número
de notas com que o aluno pretende efetuar o cálculo não será fornecido ao programa, o qual terminará quando for
introduzido um valor que não seja válido como nota de aprovação.

"""


soma = 0
n_notas = 0
media = 0

nota = int(input('Informe uma nota entre 10 e 20: '))

while True:
    nota = int(input('Informe uma nota entre 10 e 20: '))
    if 10 <= nota <= 20:
        soma += soma + nota
        n_notas += n_notas + 1
        media = soma / n_notas
    else:
        print('Programa finalizado porque você digitou uma nota inválida.')
        break
print(f'O número de notas aceitas foram {n_notas}, a soma das notas é {soma} e a sua media é: {media}.')
