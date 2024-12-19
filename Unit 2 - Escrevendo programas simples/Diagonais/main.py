def diagonais(M):
    primaria, secundaria = [], []
    resultado = []
    coluna = len(M) - 1

    for i in range(len(M)):
        primaria.append(M[i][i])
        secundaria.append(M[i][coluna - i])

    resultado.append(primaria)
    resultado.append(secundaria)

    return resultado


M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
M3 = [[1, 2], [3, 4]]
M4 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

assert diagonais(M) == [[1, 5, 9], [3, 5, 7]]
assert diagonais(M2) == [[1, 6, 11, 16], [4, 7, 10, 13]]
assert diagonais(M3) == [[1, 4], [2, 3]]
assert diagonais(M4) == [[1, 7, 13, 19, 25], [5, 9, 13, 17, 21]]
