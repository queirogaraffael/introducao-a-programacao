N = int(input())

def maior(argumento1,argumento2):
  maior = argumento1
  if argumento2>argumento1:
    maior = argumento2

  return maior

soma, contador = 0, 0

for i in range(N):
  numeros = input().split()

  if int(numeros[0])!=int(numeros[1]):
    soma+=maior(int(numeros[0]),int(numeros[1]))
    contador+=1
  
if soma==0 and contador==0:
  print(f"Não é possível calcular a média.")
else:
  media = soma/contador
  print(f"{media:.2f}")
