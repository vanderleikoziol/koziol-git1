total = 0

def incrementa():
    total = total + 1
    return total


print(incrementa())

print('-='*30)

total = 0

def incrementa():
    global total
    total = total + 1
    return total


print(incrementa())