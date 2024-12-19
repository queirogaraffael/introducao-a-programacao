def soma_acima_diagonal(m):
    controle = 1
    soma = 0
    for i in range(len(m)):
        for j in range(controle,len(m)):
            soma += m[i][j]
        controle += 1
    return soma


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

print(soma_acima_diagonal(M))
print(soma_acima_diagonal(M2))
print(soma_acima_diagonal(M3))
print(soma_acima_diagonal(M4))