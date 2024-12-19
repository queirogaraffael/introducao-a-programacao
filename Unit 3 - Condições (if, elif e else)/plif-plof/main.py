numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

soma = numero1+numero2+numero3

if soma%5==0 and soma%3==0:
  print("plifplof")
elif soma%3==0:
  print("plif")
elif soma%5==0:
  print("plof")
else:
  print(f"{soma}")