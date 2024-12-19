def maior(lista):
    maior = lista[0]

    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]

    return maior


def mat(numero_alunos):
    matriz = []
    soma = []

    for i in range(numero_alunos):
        apoio = []
        for j in range(3):
            valor = float(input())
            apoio.append(valor)
        matriz.append(apoio)

    for i in range(numero_alunos):
        som = matriz[i][1] + matriz[i][2]
        soma.append(som)

    for i in range(numero_alunos):
        matriz[i].append(soma[i])

    print(f"Maior nota: {maior(soma)}")
    print(matriz)


numero_alunos = int(input())
mat(numero_alunos)
