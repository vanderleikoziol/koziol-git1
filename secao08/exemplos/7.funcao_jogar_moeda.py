from random import random


def joga_moeda():
    valor = random()
    if valor > 0.5:
        return 'cara'
    return 'coroa'

print(joga_moeda())

print('-='*50)

def joga_moeda():
    if random() > 0.5:
        return 'cara'
    return 'coroa'

print(joga_moeda())
