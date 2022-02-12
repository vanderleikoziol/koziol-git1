"""
Minuto 11:48 da aula
"""
from sys import getsizeof

print(getsizeof('Geek'))

# Gerando uma lista com números em list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma set com números em set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma dic com números em dic comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista com números com generators
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension {list_comp} bytes')
print(f'set Comprehension {set_comp} bytes')
print(f'dic Comprehension {dic_comp} bytes')
print(f'Generator Expression {gen} bytes')


