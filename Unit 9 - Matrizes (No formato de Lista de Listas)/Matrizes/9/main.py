def soma_abaixo_diagonal(m):
    soma = 0
    controle = 1

    for i in range(1,len(m)):
        for j in range(controle):
            soma+= m[i][j]
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

print(soma_abaixo_diagonal(M))
print(soma_abaixo_diagonal(M2))
print(soma_abaixo_diagonal(M3))
print(soma_abaixo_diagonal(M4))