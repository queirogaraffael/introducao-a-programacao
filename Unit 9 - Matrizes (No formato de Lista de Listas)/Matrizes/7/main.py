def matriz():
    resultado = []
    for i in range(10):
        apoio = []
        for j in range(10):
            if i < j:
                apoio.append(2 * i + 7 * j + 2)
            elif i == j:
                apoio.append(3 * i**2 + 1)
            else:
                apoio.append(4 * i**3 + 5 * j**2 + 1)
        resultado.append(apoio)
    return resultado


# 7. Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos são da forma:
#A[i][j] = 2*i + 7*j 2 se i < j;
#A[i][j] = 3*i^2 1 se i = j ;
#A[i][j] = 4*i^3 5*j^2 + 1 se i > j.

