import math

a = int(input())
b = int(input())
c = int(input())

delta = b**2 - 4*a*c

if delta>0:
  x1 = (-b + math.sqrt(delta)) / (2*a)
  x2 = (-b - math.sqrt(delta)) / (2*a)
  print(f"x1 = {x1:.2f}")
  print(f"x2 = {x2:.2f}")
elif delta==0:
  x = (-b)/(2*a)
  print(f"x = {x:.2f}")
else:
  print("sem raizes reais")

"""
$ python eq2grau.py
3
-7
2
x1 = 2.00
x2 = 0.33
$ python eq2grau.py
-1
4
-4
x = 2.00"""