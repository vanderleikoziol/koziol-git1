"""
Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores que 100. Escolha
números menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta: Qual a soma de a + b,
onde a e b são números aleatórios. Peça a resposta. Faça 5 perguntas ao aluno, e mostre as perguntas e as respostas
corretas, além de quantas vezes o aluno acertou.

"""


import random


print('PROVA DE MATEMÁTICA')
print('_' * 20)

# Pergunta 01


a = random.randint(1, 100)
b = random.randint(1, 100)
s1 = a + b
print(f'Qual a soma de {a} + {b}?')
r1 = int(input('Informe o valor: '))
if s1 == r1:
    p1 = 1
    print('Correta')
else:
    p1 = 0
    print('Errada')

# Pergunta 02


a = random.randint(1, 100)
b = random.randint(1, 100)
s2 = a + b
print(f'Qual a soma de {a} + {b}?')
r2 = int(input('Informe o valor: '))
if s2 == r2:
    p2 = 1
    print('Correta')
else:
    p2 = 0
    print('Errada')

# Pergunta 03


a = random.randint(1, 100)
b = random.randint(1, 100)
s3 = a + b
print(f'Qual a soma de {a} + {b}?')
r3 = int(input('Informe o valor: '))
if s3 == r3:
    p3 = 1
    print('Correta')
else:
    p3 = 0
    print('Errada')

# Pergunta 04


a = random.randint(1, 100)
b = random.randint(1, 100)
s4 = a + b
print(f'Qual a soma de {a} + {b}?')
r4 = int(input('Informe o valor: '))
if s4 == r4:
    p4 = 1
    print('Correta')
else:
    p4 = 0
    print('Errada')


# Pergunta 05


a = random.randint(1, 100)
b = random.randint(1, 100)
s5 = a + b
print(f'Qual a soma de {a} + {b}?')
r5 = int(input('Informe o valor: '))
if s5 == r5:
    p5 = 1
    print('Correta')
else:
    p5 = 0
    print('Errada')


acertos = p1 + p2 + p3 + p4 + p5


print(f"Pergunta 01: Você respondeu {r1} e a resposta correta é {s1}.\nPergunta 02: Você respondeu {r2} e a resposta "
      f"correta é {s2}.\nPergunta 03: Você respondeu {r3} e a resposta correta é {s3}.\nPergunta 04: Você respondeu "
      f"{r4} e a resposta correta é {s4}.\nPergunta 05: Você respondeu {r5} e a resposta correta é {s5}.")
print(f'Você acertou {acertos} respostas de um total de 5 perguntas.')