def busca_matriz(m, e):
    resultado = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == e:
                resultado.append((i, j))
    return resultado


matriz = [[2, 3, 5, 3, 1], [3, 2, 1, 5, 6], [1, 2, 3, 2, 1]]
assert busca_matriz(matriz, 4) == []
assert set(busca_matriz(matriz, 3)) == set([(0, 1), (0, 3), (1, 0), (2, 2)])
assert set(busca_matriz(matriz, 1)) == set([(0, 4), (1, 2), (2, 0), (2, 4)])
