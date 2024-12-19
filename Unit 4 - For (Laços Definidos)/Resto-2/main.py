N = int(input())

lista = list(range(1,10001))

for i in lista:
    if i%N==2:
        print(i)