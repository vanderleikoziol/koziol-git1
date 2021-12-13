"""
Como indexar uma tabela ASCCII para poder contar o número de ocorrência de uma letra.

"""

for i in range(65, 91):
    idx = ord(chr(i)) - ord('A')
    print(f'{idx}: {chr(i)}')

for i in range(97, 123):
    idx = ord(chr(i)) - ord('a')
    print(f'{idx}: {chr(i)}')
