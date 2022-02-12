valores = {}
n = 0

while n < 5:
    y = int(input(f'Informe o valor {n+1}/5: '))
    n += 1
    valores[n] = y

sum(valores.values())
len(valores)
media = sum(valores.values()) / len(valores)
print(f'Os valores lidos são: {valores}\nO maior valor é: {max(valores.values())}\nO menor valor é: '
      f'{min(valores.values())}\nA média dos valores é: {media:.2f}')

