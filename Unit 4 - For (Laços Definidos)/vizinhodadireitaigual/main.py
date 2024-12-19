sequencia = input().split()

sequencia_int = []

for i in range(len(sequencia)):
  sequencia_int.append(int(sequencia[i]))

soma = 0

for i in range(len(sequencia_int)):
    if i != (len(sequencia_int)-1) and (sequencia_int[i] == sequencia_int[i+1]):
      soma+=1
print(soma)