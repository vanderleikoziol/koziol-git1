"""
Faça um programa para calcular a seguintes sequências.
1 + 2 + 3 + 4 + 5 + ...+ n
1 + 2 + 3 + 4 + 5 + ...+ (2n - 1)
1 + 3 + 5 + 7 + ...+ (2n - 1)

"""
s1 = 0
s2 = 0
s3 = 0
soma1 = 0
soma2 = 0
soma3 = 0
n = int(input('Informe um número: '))

for i in range(1, n + 1, 1):
    if i % 2 == 0:
        s1 += i
        soma1 = s1 + n
        s2 += i
        soma2 = s2 + ((2 * n) - 1)
        s3 += 0
    else:
        s3 += i
        soma3 = s3 + ((2 * n) - 1)

print(f'A soma da sequência 1 é: {soma1}.')
print(f'A soma da sequência 2 é: {soma2}.')
print(f'A soma da sequência 3 é: {soma3}.')
