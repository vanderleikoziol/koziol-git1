arquivo = open('texto.txt')

print(arquivo.read())
print(arquivo.closed)


arquivo.close()
print(arquivo.closed)
