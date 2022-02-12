import os
import sys
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
print(os.path.isabs('/home/geek/'))
print(os.name)
print(os.uname())
print(sys.platform)
# '/home/geek/workspace/sistema'

print(os.getcwd())

res = os.path.join(os.getcwd(), 'geek')
os.chdir(res)

print(os.getcwd())

arquivos = list(os.scandir(0))
print(arquivos)
print(dir(arquivos[0]))
print(arquivos[0].inode())  # numeração do elemento na arvore de diretórios
print(arquivos[0].is_dir())  # é um diretório? False
print(arquivos[0].is_file())  # é um arquivo? True
print(arquivos[0].is_symlink())  # é um link simbólico? False
print(arquivos[0].name())  # caminho até o arquivo
print(arquivos[0].ispath())  # informações statisticas do arquivo





