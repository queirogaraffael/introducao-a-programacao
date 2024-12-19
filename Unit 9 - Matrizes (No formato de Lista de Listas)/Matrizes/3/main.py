def matriz(m1, m2):
    resultado = []
    for i in range(len(m1)):
        apoio = []
        for j in range(len(m1[0])):
            produto = m1[i][j] * m2[i][j]
            apoio.append(produto)
        resultado.append(apoio)
    return resultado


# 3. Faça um programa que preenche uma matriz com o produto do valor da linha e da coluna
# de cada elemento. Em seguida, imprima na tela a matriz.

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print(matriz(m1, m2))
