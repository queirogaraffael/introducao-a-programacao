def ordena(numeros, nomes):
    if len(nomes) >= 2:
        for i in range(len(nomes) - 1):
            for j in range(len(nomes) - i - 1):
                if nomes[j] > nomes[j + 1]:
                    nomes[j], nomes[j + 1] = nomes[j + 1], nomes[j]
                    numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]


def dentro(nome, lista):
    for i in range(len(lista)):
        if nome == lista[i]:
            return True
    return False


nomes, numeros = [], []
nomes_buscas = []
imprimir = False

while True:
    opcao = input()
    if opcao == "finalizar": break

    if opcao == "inserir":
        repeticoes = int(input())
        for i in range(repeticoes):
            nome = input()
            numero = int(input())
            if not dentro(numero, numeros):
              nomes.append(nome)
              numeros.append(numero)
    elif opcao == "buscar":
        nomes_buscas.append(input())
    else:
        imprimir = True

ordena(numeros, nomes)

for i in range(len(nomes_buscas)):
    if dentro(nomes_buscas[i], nomes):
        for j in range(len(nomes)):
            if nomes[j] == nomes_buscas[i]:
                print(f"Nome: {nomes[j]}")
                print(f"Fone: {numeros[j]}")
                print("----------")
    else:
        print("Nome inexistente")
        print("----------")

if imprimir:
    for i in range(len(nomes)):
        print(f"Nome: {nomes[i]}")
        print(f"Fone: {numeros[i]}")
        print("----------")


inserir
2
raffael
96949169
raffael
96949169
buscar
raffael
imprimir
finalizar
Nome: raffael
Fone: 96949169
----------
Nome: raffael
Fone: 96949169
----------
Nome: raffael
Fone: 96949169
----------
Nome: raffael
Fone: 96949169
----------