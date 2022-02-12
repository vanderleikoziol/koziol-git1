import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'Arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
        input()