"""
ceil  => arredonda para cima
floor => arredonda para baicho
trunc => elimina da vírgula para frente
pow => potência
sqrt => square root (raź quadrada)
factorial => para calcular fatorial

from math import sqrt => vai importar somente a raíz quadrada


"""
import math

num = int(input('Digite um número: '))

raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é {raiz:.0f}.')

