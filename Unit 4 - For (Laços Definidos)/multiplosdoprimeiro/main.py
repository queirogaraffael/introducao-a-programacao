primeiro = int(input())

soma = 0 

for i in range(10):
  numeros = int(input())
  if numeros%primeiro ==0:
    soma+=numeros

print(soma)
