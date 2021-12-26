"""
Se os números de 1 a 5 são escritos em palavras: um, dois, três, quatro, cinco, então há 2 + 4 + 4 + 6 + 5 = 22 letras
usadas no total. Faça um progra que conte quantas letras seriam utilizadas se todos os números de 1 a 1000 (mil)
fossem escritos em palavras. Obs. Não conte espaços nem hifens.

"""


from num2words import num2words

total = ""

for n in range(1, 1001):
    num = num2words(n, lang='pt-BR')
    total += num.replace(' ', '')

print(f'Entre 1 e 1000 temos {len(total)} letras.')
