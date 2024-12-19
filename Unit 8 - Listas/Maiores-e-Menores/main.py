menores = []
maiores = []

pivot = int(input())

while True:
  numero = int(input())
  if numero < 0:break
  
  if numero<=pivot:
    menores.append(numero)
  else:
    maiores.append(numero)

print(menores)
print(pivot)
print(maiores)


4
8
3
9
2
0
5
-1
[3, 2, 0]
4
[8, 9, 5]
