posicao = 1
treze, campinense = 0, 0
trezeano, raposeiros = [], []

while True:
    nome = input()
    if nome == "t":
        trezeano.append(posicao)
        treze += 1
    else:
        raposeiros.append(posicao)
        campinense += 1
    if abs(campinense - treze) > 2:
        if campinense > treze:
            print("RAPOSEIROS em maior quantidade")
        else:
            print("TREZEANOS em maior quantidade")
        break
    posicao += 1

print("TREZEANOS:")
for i in range(len(trezeano)):
    print(trezeano[i])

print("RAPOSEIROS:")
for i in range(len(raposeiros)):
    print(raposeiros[i])
"""
t
c
t
t
t
TREZEANOS em maior quantidade
TREZEANOS:
1
3
4
5
RAPOSEIROS:
2

"""
