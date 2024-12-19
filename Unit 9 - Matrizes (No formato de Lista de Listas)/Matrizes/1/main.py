def conta_matriz(M, numero):
    contador = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] > numero:
                contador += 1
    return contador


# 1. Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 #ela possui.

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
M3 = [[1, 2], [3, 4]]
M4 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

print(conta_matriz(M, 10))
print(conta_matriz(M2, 3))
print(conta_matriz(M3, 4))
print(conta_matriz(M4, 1))
