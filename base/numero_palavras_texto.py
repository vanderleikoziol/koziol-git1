"""
Este comando eu utilizo para verificar quantas vezes uma palavra se repete em um texto.

"""


from collections import Counter
texto = """O Bismarck foi o primeiro navio couraçado alemão da Classe Bismarck operado pela Kriegsmarine. Batizado em homenagem
 ao chanceler Otto von Bismarck, um dos grandes responsáveis pela unificação da Alemanha em 1871, teve sua construção 
iniciada nos estaleiros da Blohm & Voss em 1º de julho de 1936, sendo lançado ao mar dois anos e meio depois, em 14 de 
fevereiro de 1939. Foi finalizado e comissionado para a frota alemã em 24 de agosto de 1940. O Bismarck e o seu irmão 
Tirpitz foram os maiores navios de guerra construídos pela Alemanha Nazi, e dois dos maiores navios construídos por uma 
potência europeia."""

palavras = texto.split()
print(palavras)

res = Counter(palavras)
print((res))

print(f'As 5 palavras que mais se repetem são:\n{res.most_common(5)}')
