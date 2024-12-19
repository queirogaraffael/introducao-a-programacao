brasil = input().split()
italia = input().split()

brasill = []
italiaa = []

for i in range(len(brasil)):
    brasill.append(int(brasil[i]))

for i in range(len(italia)):
    italiaa.append(int(italia[i]))

ouro_brasil, prata_brasil, bronze_brasil = 0, 0, 0
ouro_italia, prata_italia, bronze_italia = 0, 0, 0

for i in range(len(brasill)):
    if brasill[i] == 0:
        ouro_brasil += 1
    elif brasill[i] == 1:
        prata_brasil += 1
    else:
        bronze_brasil += 1

for i in range(len(italiaa)):
    if italiaa[i] == 0:
        ouro_italia += 1
    elif italiaa[i] == 1:
        prata_italia += 1
    else:
        bronze_italia += 1

if ouro_brasil > ouro_italia:
    print("brasil")
elif ouro_italia > ouro_brasil:
    print("italia")
elif prata_brasil > prata_italia:
    print("brasil")
elif prata_italia > prata_brasil:
    print("italia")
elif bronze_brasil > bronze_italia:
    print("brasil")
elif bronze_italia > bronze_brasil:
    print("italia")
elif ouro_brasil == ouro_italia:
    print("empate")
elif bronze_brasil == bronze_italia:
    print("empate")
else:
    print("empate")