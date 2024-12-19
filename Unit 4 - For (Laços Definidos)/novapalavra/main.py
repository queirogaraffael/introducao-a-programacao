palavra = list(input())
numero = list(input())

numeros = []
nova_palavra = []

for i in range(len(numero)):
    numeros.append(int(numero[i]))

for i in range(len(numero)):
    nova_palavra.append((numeros[-i - 1] + 1) * palavra[i])

nome = "".join(nova_palavra)
print(nome)