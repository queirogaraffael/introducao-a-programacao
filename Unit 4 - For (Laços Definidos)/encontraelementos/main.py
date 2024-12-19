numero = int(input())
sequencia = input().split()

sequencia_int =[]
sim = 0

for i in range(len(sequencia)):
  sequencia_int.append(int(sequencia[i]))

  if sequencia_int[i] == numero:
    sim +=1

if sim>=1:
  print("Sim")
else:
  print("Não")