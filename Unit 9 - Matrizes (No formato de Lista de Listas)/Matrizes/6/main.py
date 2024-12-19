def matriz_maior(m1, m2):
    matriz_final = []

    for i in range(len(m1)):
        apoio = []
        for j in range(len(m1[0])):
            if m1[i][j] > m2[i][j]:
                apoio.append(m1[i][j])
            else:
                apoio.append(m2[i][j])
        matriz_final.append(apoio)
    return matriz_final


# Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores valores de cada posição
# das matrizes lidas.

M1 = [[1, 2, 3], [13, 14, 15], [7, 8, 9]]
M2 = [[10, 11, 12], [4, 5, 6], [7, 8, 9]]
M3 = [[1, 2, 3], [0, 0, 0], [7, 8, 9]]
assert matriz_maior(M1, M2) == [[10, 11, 12], [13, 14, 15], [7, 8, 9]]
assert matriz_maior(M1, M3) == [[1, 2, 3], [13, 14, 15], [7, 8, 9]]
assert matriz_maior(M2, M3) == [[10, 11, 12], [4, 5, 6], [7, 8, 9]]