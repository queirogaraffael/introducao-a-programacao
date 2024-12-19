n = int(input())

soma = []
soma1 = 0

while True:
  numero = input().split()
  x = int(numero[0])
  y = int(numero[1])
  if x>y:
    for i in range(y+1,x):
      if i%2!=0:
        soma1+=i
    soma.append(soma1)
  else:
    for i in range(x+1,y):
      if i%2!=0:
        soma1+=i
    soma.append(soma1)
  soma1=0
  n-=1
  if n<=0:break


for i in soma:
  print(i)

"""
7
4 5
13 10
6 4
3 3
3 5
3 4
3 8

0
11
5
0
0
0
12
"""

