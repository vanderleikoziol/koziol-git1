"""
Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou por 5, mas não simultâneamente
pelos dois.

a) Modelo 1 de solução.

n = int(input('Informe um número: '))

if n % 3 == 0 and n % 5 != 0:
    print(f'O número {n} é divisível por 3 mas não é divisível por 5:')
elif n % 5 == 0 and n % 3 != 0:
    print(f'O número {n} é divisível por 5 mas não é divisível por 3.')
elif n % 3 == 0 and n % 5 == 0:
    print(f'O Número é divisível por 3 e 5 simultâneamente.')
else:
    print(f'O número não é divisível por 3 ou por 5.')

"""
# Modelo 2 de solução.

n = int(input('Informe um número: '))

var = n % 3 == 0 and n % 5 == 0
print(var)
if var == True:
    print(f'Não atende os requisitos:')
elif var == False:
    nova_verificacao = n % 3 == 0 or n % 5 == 0
    print(nova_verificacao)
    if nova_verificacao == True:
        print(f'Atende os requisitos:')
    else:
        print(f'Não atende os requisitos:')

