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

n = 0

for i in lista:
  if i%2==0:
    n +=1

print(f"{n} valores pares")