lista = []

numero1 = int(input())
numero2 = int(input())
numero3 = int(input())
numero4 = int(input())
numero5 = int(input())

lista.append(numero1)
lista.append(numero2)
lista.append(numero3)
lista.append(numero4)
lista.append(numero5)

par = 0
impar = 0
positivo = 0
negativo = 0

for i in lista:
  if i%2==0:
    par +=1
  
  if i%2!=0:
    impar+=1
  
  if i>0:
    positivo+=1
  
  if i<0:
    negativo+=1

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")