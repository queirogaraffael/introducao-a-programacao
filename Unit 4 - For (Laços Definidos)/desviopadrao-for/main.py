import math

lista1 = input().split(" ")
lista2 = input().split(" ")

lista11 =[]
lista22 =[]

soma1 = 0
soma2 = 0

for i in range(len(lista1)):
  lista11.append(float(lista1[i]))
  soma1 += lista11[i]

for i in range(len(lista2)):
  lista22.append(float(lista2[i]))
  soma2 += lista22[i]

media1 = soma1 / len(lista1)
media2 = soma2 / len(lista2)

variancia1 = 0
variancia2 = 0

for i in range(len(lista1)):
  variancia1 += ((lista11[i]-media1)**2)

for i in range(len(lista2)):
  variancia2 += ((lista22[i]-media2)**2)

variancia11 = variancia1/(len(lista1)-1)
variancia22 = variancia2/(len(lista2)-1)

DP1 = math.sqrt(variancia11)
DP2 = math.sqrt(variancia22)

if DP1>DP2:
  print(f"A sequência 1 possui o maior desvio padrão ({DP1:.2f}).")
elif DP2>DP1:
  print(f"A sequência 2 possui o maior desvio padrão ({DP2:.2f}).")
else:
  print(f"As sequências possuem o mesmo desvio padrão ({DP2:.2f}).")


