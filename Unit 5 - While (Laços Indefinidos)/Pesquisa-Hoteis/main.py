valor, tamanho, conforto, nomes = [], [], [], []


def maior(lista):
    indice = 0
    maior = lista[0]
    for i in range(1, len(lista)):
        if maior < lista[i]:
            maior = lista[i]
            indice = i
    return indice


while True:
    entrada = input().split(",")
    if entrada[0] == "---": break

    valor.append(float(entrada[0]))
    tamanho.append(float(entrada[1]))
    conforto.append(float(entrada[2]))
    nomes.append(entrada[3])

while True:
    entrada2 = input()
    if entrada2 == "fim": break

    if entrada2 == "valor":
        menor = valor[0]
        indice = 0
        for i in range(1, len(valor)):
            if menor > valor[i]:
                menor = valor[i]
                indice = i
        print(nomes[indice])
    elif entrada2 == "tamanho":
        indice = maior(tamanho)
        print(nomes[indice])
    else:
        indice = maior(conforto)
        print(nomes[indice])
"""

2000.0,1,16,h1
4000.0,4,7,h2
1900.0,6,23,h3
1500.0,3,5,h4
8000.0,0,1,h5
---
valor
h4
tamanho
h3
conforto
h3
fim"""
