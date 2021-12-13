"""
Escreva um programa de ajuda para vendedores. A partir de um valor total lido, motre:
a) O total a pagar com desconto de 10%;
b) O valor de cada parcela no parcelamento de 3 x sem juros;
c) A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto);
d) A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

"""

# Entradas


valor = int(input('Informe o valor da venda R$ '))


# Processamento

desconto = valor * (10 / 100)
a = valor - desconto
b = valor / 3
c = a * (5 / 100)
d = valor * (5 / 100)

# Saída


print(f'a) O valor a pagar com desconto de 10% é R$ {a:.2f}.')
print(f'b) O valor de cada parcela no parcelamento em 3 x sem juros é R$ {b:.2f}.')
print(f'c) O valor de comissão de 5% para venda a vista é R$ {c:.2f}.')
print(f'd) O valor de comissão de 5% para venda parcelada é R$ {d:.2f}.')

