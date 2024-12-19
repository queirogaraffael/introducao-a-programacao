n = int(input())

lista2 = []

for i in range(n):
  n1 = int(input())
  lista2.append(n1)

for i in lista2:
  if i<0 and i%2!=0:
    print("ODD NEGATIVE")
  elif i==0:
    print("NULL")
  elif i>0 and i%2!=0:
    print("ODD POSITIVE")
  elif i<0 and i%2==0:
    print("EVEN NEGATIVE")
  else:
    print("EVEN POSITIVE")

