x = []
y = []
z = []
p = []
n = 0

for i in range(5):
    x.append(int(input(f'Informe o valor {i + 1}/5 do vetor x: ')))
    y.append(int(input(f'Informe o valor {i + 1}/5 do vetor y: ')))
print(f'Os valores do vetor x é: {",".join(map(str,x))}')
print(f'Os valores do vetor y é: {",".join(map(str,y))}')
x1, x2, x3, x4, x5 = x
y1, y2, y3, y4, y5 = y
z.append(x1 + y1), z.append(x2 + y2), z.append(x3 + y3), z.append(x4 + y4), z.append(x5 + y5)
p.append(x1 * y1), p.append(x2 * y2), p.append(x3 * y3), p.append(x4 * y4), p.append(x5 * y5)
dfx = set(x)
dfy = set(y)
sox = dfx.difference(dfy)
iterxy = dfx.intersection(dfy)
unixy = dfy.union(dfx)
print(f'A soma entre x e y é:{",".join(map(str,z))}')
print(f'O produto entre x e y é:{",".join(map(str,p))}')
print(f'Os elementos que só existem em x são: {",".join(map(str,sox))}')
print(f'Os elementos que aparecem em x e y são: {",".join(map(str,iterxy))}')
print(f'A união de x e y que não estão em x é: {",".join(map(str,unixy))}')
