N = int(input())

lista = list(range(N))

media = list(range(N))

for i in lista:
  numero = input()
  numero = numero.split()
  numero1 = float(numero[0])
  numero2 = float(numero[1])
  numero3 = float(numero[2])

  media[i] = (numero1*2 +numero2*3 +numero3*5)/10


for i in lista:
  print(f"{media[i]:.1f}")
