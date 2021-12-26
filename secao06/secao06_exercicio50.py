"""
Chico tem 1.5 metro e cresce 2 centímetros por ano, equanto Zé tem 1.10 metros e cresce 3 centímetros por ano.
Escreva um programa que calcule e imprima quantos anos serão necessários para que zé seja maior que Chico.

"""
ac = 1.5 * 100
az = 1.1 * 100
cont = 0
while True:
    cont += 1
    ac += 2
    az += 3
    if az > ac:
        break
print(f'Daqui a {cont} anos Zé terá {az/100:.2f} metros e Chico terá {ac/100:.2f} metros.')
