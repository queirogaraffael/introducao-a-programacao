frase = list(input())
indice = int(input())
j = int(input())

lista = []

for i in range(indice, j):
    if frase[i] != " " and not i == (j - 1):
        lista.append(f"{frase[i]} ")
    elif i == (j - 1):
        if frase[i] == " ":
            lista.append(",")
        else:
            lista.append(f"{frase[i]}")
    else:
        lista.append(", ")

nome = "".join(lista)

print(nome)
