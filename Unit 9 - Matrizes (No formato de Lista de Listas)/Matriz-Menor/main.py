def matriz_menor(matriz1, matriz2):
    resultado = []

    for i in range(len(matriz1)):
        matriz_apoio = []
        for j in range(len(matriz1[0])):
            if matriz1[i][j] <= matriz2[i][j]:
                matriz_apoio.append(matriz1[i][j])
            else:
                matriz_apoio.append(matriz2[i][j])
        resultado.append(matriz_apoio)

    return resultado


M1 = [[1, 2, 3], [13, 14, 15], [7, 8, 9]]
M2 = [[10, 11, 12], [4, 5, 6], [7, 8, 9]]
M3 = [[1, 2, 3], [0, 0, 0], [7, 8, 9]]
assert matriz_menor(M1, M2) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert matriz_menor(M1, M3) == [[1, 2, 3], [0, 0, 0], [7, 8, 9]]
assert matriz_menor(M2, M3) == [[1, 2, 3], [0, 0, 0], [7, 8, 9]]
