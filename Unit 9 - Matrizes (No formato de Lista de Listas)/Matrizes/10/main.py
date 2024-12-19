def soma_diagonal(m):
    soma = 0
    for i in range(len(m)):
        soma += m[i][i]
    return soma


# 10. Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão na diago-nal principal.


M = [[1, 2, 3], 
    [4, 5, 6],
     [7, 8, 9]]

M2 = [[1, 2, 3, 4], 
      [5, 6, 7, 8], 
      [9, 10, 11, 12], 
      [13, 14, 15, 16]]

M3 = [[1, 2], 
      [3, 4]]

M4 = [[1, 2, 3, 4, 5], 
     [6, 7, 8, 9, 10], 
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20], 
     [21, 22, 23, 24, 25]]

print(soma_diagonal(M))
print(soma_diagonal(M2))
print(soma_diagonal(M3))
print(soma_diagonal(M4))