def ordena(lista):
    if len(lista) >= 2:
        for i in range(len(lista) - 1):
            for j in range(len(lista) - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]


lista_nomes = []
lista_ordenada = []

while True:
    nome = input()
    if nome == "####": break
    lista_nomes.append(nome)

for i in range(len(lista_nomes)):
    lista_ordenada.append(lista_nomes[i])
    ordena(lista_ordenada)

    for j in range(len(lista_ordenada)):
        if lista_ordenada[j] == lista_nomes[i]:
            print(f"* {lista_ordenada[j]}")
        else:
            print(lista_ordenada[j])

    print("----")
