"""
Escreva um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem a propriedade seguinte: a soma
dos dois dígitos de mais baixa ordem com os dois dígitos de mais alta ordem elevado ao quadrado é igual ao próprio
número. Por exemplo, para o inteiro 3025, temos que:
 30 + 25 = 55
 55 ** 2 = 3025
"""
lista = []

for i in range(1000, 9999 + 1, 1):
    string = str(i)
    ordem1 = int(string[0:2])
    ordem2 = int(string[2:4])
    soma = ordem1 + ordem2
    if soma**2 == i:
        lista.append(i)
print(f'Os números que atendem a condição são: {lista}. ')

        