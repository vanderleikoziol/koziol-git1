import os
import tempfile

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

""" criando sem o with"""

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

""" outra forma"""

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')
print(arquivo.name)
print(arquivo.read())

input()
arquivo.close()

