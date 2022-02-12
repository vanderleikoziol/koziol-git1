a = []
b = []
c = []

for i in range(5):
    a.append(int(input(f'Informe o valor de conj 1 na posição {i}: ')))
    b.append(int(input(f'Informe o valor do conj 2 na posição {i}: ')))
for i in range(len(a)):
    c.append(a[i] * b[i])

print(f"O primeiro conjunto é: {str(a).strip('[]')}.\nO segundo conj é: {str(b).strip('[]')}.\nO produto escalar é: "
      f"{str(c).strip('[]')}.")
