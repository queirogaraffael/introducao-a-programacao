import math

inicial = float(input())
delta = float(input())
N = int(input())

dados = []
tangente = []

for i in range(N):
  if i == 0:
     dados.append(inicial)
  else:
     dados.append(inicial+delta*i)


for i in range(N):
  tangente.append(math.tan(math.radians(dados[i])))
  print(f"{dados[i]:.2f} {tangente[i]:.4f}")

"""
30.00 0.5774
30.60 0.5914
31.20 0.6056
31.80 0.6200
32.40 0.6346"""