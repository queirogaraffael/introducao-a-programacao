def matriz(m,x):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == x:
              return (i,j)

    return 'não encontrado'


# 5. Leia uma matriz 5 x 5. Leia também um valor X. O programa deverá fazer uma busca
#desse valor na matriz e, ao final, escrever a localização (linha e coluna) ou uma mensa-
#gem de “não encontrado”.

M = [[1, 9, 3], [4, 5, 6], [7, 8, 9]]
M2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
M3 = [[1, 2], [3, 4]]
M4 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

print(matriz(M,1))
print(matriz(M2,16))
print(matriz(M3,2))
print(matriz(M4,0))