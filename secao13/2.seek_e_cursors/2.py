arquivo = open('texto.txt')

# print(arquivo.readline())

ret = arquivo.readline()

print(type(ret))
print(ret)
print(ret.split(' '))
