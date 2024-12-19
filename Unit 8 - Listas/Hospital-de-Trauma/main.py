def ordena(numeros, nomes):
    if len(numeros) >= 2:
        for i in range(len(numeros) - 1):
            for j in range(len(numeros) - i - 1):
                if numeros[j] > numeros[j + 1]:
                    nomes[j], nomes[j + 1] = nomes[j + 1], nomes[j]
                    numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]


def contador(num, lista):
    cont = 0
    for i in range(len(lista)):
        if lista[i] == num:
            cont += 1
    return cont


def cadastra(fila, nome, prioridade):
    fila.append(nome)
    ordena(prioridade, fila)


def resumo():
    print("---")
    for i in range(1, 6):
        cont = contador(i, codigo)
        if i == 1:
            print(f"vermelho: {cont}")
        elif i == 2:
            print(f"laranja: {cont}")
        elif i == 3:
            print(f"amarelo: {cont}")
        elif i == 4:
            print(f"verde: {cont}")
        else:
            print(f"azul: {cont}")
    print("---")


codigo, nomes, fila = [], [], []

while True:
    nome = input().split()
    if nome[0] == "fim": break

    nomes.append(nome[0])

    if nome[1] == "vermelho":
        codigo.append(1)
    elif nome[1] == "laranja":
        codigo.append(2)
    elif nome[1] == "amarelo":
        codigo.append(3)
    elif nome[1] == "verde":
        codigo.append(4)
    else:
        codigo.append(5)

    cadastra(fila, nome[0], codigo)

for i in range(len(fila)):
    print(f"{fila[i]}")

resumo()
"""
José azul
Joana verde
Tonho vermelho
Maria laranja
Severino vermelho
Ana vermelho 
fim
Tonho
Severino
Ana
Maria
Joana
José
---
vermelho: 3
laranja: 1
amarelo: 0
verde: 1
azul: 1
---
"""
