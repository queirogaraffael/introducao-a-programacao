nome = input()

numeros = ""

for i in nome:
    if i in "13579":
        numeros += str(i) + " "

numeros = numeros.split()
soma = 1

for i in range(len(numeros)):
    soma *= int(numeros[i])

soma = str(soma)

print(f"{soma}")

"""
a1bc2x3yy45z
15"""
