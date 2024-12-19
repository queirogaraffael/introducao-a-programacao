lista = []

numero1 = float(input())
numero2 = float(input())
numero3 = float(input())
numero4 = float(input())
numero5 = float(input())
numero6 = float(input())

lista.append(numero1)
lista.append(numero2)
lista.append(numero3)
lista.append(numero4)
lista.append(numero5)
lista.append(numero6)

n = 0

for i in lista:
  if i>0:
    n += 1

print(f"{n} valores positivos")