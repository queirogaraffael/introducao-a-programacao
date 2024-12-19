k = int(input())
n = int(input())

soma = 0 

for i in range(n): 
  numero = int(input())
  if i%k==0:
    soma+=numero

print(f"Soma: {soma}.")