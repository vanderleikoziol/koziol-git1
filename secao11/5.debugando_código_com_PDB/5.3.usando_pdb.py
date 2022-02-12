
"""
l = > listar onde estamos no código
n => próxima linha
p => imprime variável
c => continua a execução - finaliza o debugging
"""
# Exemplo 1
import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Esencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo 2
nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Esencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo 3
nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Esencial'
final = nome_completo + ' faz o curso ' + curso
print(final)