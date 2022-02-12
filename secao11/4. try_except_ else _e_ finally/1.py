num = 0
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')

print(f'Você digitou {num}')


print('-='*30)
try:
    num = int(input('Informe um número: '))  # 13:35 min
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')



print('-='*30)
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o Finally')





