numero = int(input())

lista = list(range(numero,numero+12))

for i in lista:
    if i%2!=0:
        print(i)