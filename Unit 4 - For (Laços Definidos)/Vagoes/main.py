K = int(input())
sequencia = input().split()

controle = 0

for i in range(len(sequencia)):
  if i != (len(sequencia) - 1) and abs(int(sequencia[i]) - int(sequencia[i+1]))>K:
      controle+=1
    
print(controle)
