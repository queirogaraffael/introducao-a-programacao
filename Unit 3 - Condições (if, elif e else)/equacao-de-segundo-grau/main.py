import math

print("Equações de 2o grau")
a = int(input("a? "))
b = int(input("b? "))
c = int(input("c? "))

print(f"equação: {a}x2 + {b}x + {c} = 0")

delta = pow(b,2) - 4 * a * c

print(f"delta = {delta:.2f}")

if delta < 0:
   print("equação sem raízes reais")
elif delta == 0:
  print("uma raíz real")
  x1 = (-b + math.sqrt(delta))/ (2*a)
  print(f"x2 = {x2:.2f}")
else:
  x1 = (-b + math.sqrt(delta))/ (2*a)
  x2 = (-b - math.sqrt(delta))/(2*a)
   print("duas raízes reais")
   print(f"x1 = {x1:.2f}")
   print(f"x2 = {x2:.2f}")