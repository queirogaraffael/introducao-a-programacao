lucro = []

for i in range(12):
  numero = input().split()
  lucro.append((float(numero[0]))-(float(numero[1])))

meses = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"]

for i in range(12):
  if lucro[i]<0:
    print(f"{meses[i]} {lucro[i]:.1f}")
  else:
    print(f"{meses[i]}  {lucro[i]:.1f}")