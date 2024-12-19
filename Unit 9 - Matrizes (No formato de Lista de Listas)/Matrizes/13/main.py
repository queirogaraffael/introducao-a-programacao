def matriz():
    matriz = []
    matriz_base = []
    valor = 1

    for i in range(4):
        apoio = []
        for j in range(4):
            apoio.append(valor)
            valor += 1
        matriz.append(apoio)

    for i in range(len(matriz)):
        apoio = []
        for j in range(len(matriz[0])):
            apoio.append(matriz[i][j])
        matriz_base.append(apoio)

    inicio = 1

    for i in range(len(matriz) - 1):
        for j in range(inicio, len(matriz)):
            matriz_base[i][j] = 0
        inicio += 1

    print(matriz)
    print("---")
    print(matriz_base)


# Gere matriz 4 x 4 com valores no intervalo [1, 20]. Escreva um programa que transforme
#a matriz gerada numa matriz triangular inferior, ou seja, atribuindo zero a todos os ele-
#mentos acima da diagonal principal. Imprima a matriz original e a matriz transformada.
