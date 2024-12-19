nomes = input().split()

fora_de_ordem = -1

for i in range(len(nomes)):
    if i != (len(nomes) - 1) and nomes[i] > nomes[i + 1]:
        fora_de_ordem = i

if fora_de_ordem >= 0:
    print(f"fora de ordem: {i}")
else:
    print("em ordem")


"""
a b c d e f ok

f e d c b a

caso dado abacate tatu ok

tatu dado abacate casook
dado empresa tatu ok
"""