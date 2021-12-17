"""
Tabela de emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode

Original: U+1F60D
Modificado: U0001F60D => mantém o U e acrescenta  3 zeros e replica o resto do código.

Para executar 1 vez
    for num in range(1, 11):
        print('\U0001F60D' * num)
Se quiser executar 3 vezes
for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)

"""


for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)
