def matriz(m):
    maior = m[0][0]
    indice = (0, 0)

    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] >= maior:
                maior = m[i][j]
                indice = (i, j)

    return indice


# Leia uma matriz 4 x 4, imprima a matriz e retorne a localização (linha e a coluna) do
# maior valor.

M = [[1, 9, 3], [4, 5, 6], [7, 8, 9]]
M2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
M3 = [[1, 2], [3, 4]]
M4 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

print(matriz(M))
print(matriz(M2))
print(matriz(M3))
print(matriz(M4))
