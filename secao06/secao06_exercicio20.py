"""
Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número de dados
lidos e número de valores pares. O processo termina quando digitado o número 1000.

"""
cont_total = 0
cont_par = 0
numero = int(input('Informe um número: '))

while numero != 1000:
    numero = int(input('Informe um número: '))
    cont_total = cont_total + 1
    if numero % 2 == 0:
        cont_par = cont_par + 1
print(f'Foram lidos o total de {cont_total} entradas e {cont_par} são números pares.')
