def matriz_transposta(m):
    resultado = []
    for j in range(len(m[0])):
        apoio = []
        for i in range(len(m)):
            apoio.append(m[i][j])
        resultado.append(apoio)
    return resultado


# 12. Leia uma matriz de 3 x 3 elementos. Calcule e imprima a sua transposta.

m = [[1, 5], [7, 2], [8, 2]]
print(matriz_transposta(m))

m = [[8, 2], [7, 2], [1, 5]]
print(matriz_transposta(m))