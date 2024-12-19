def secundaria(m):
    soma = 0
    controle = len(m) - 1
    for i in range(len(m)):
        soma += m[i][controle]
        controle -= 1
    return soma


# 11. Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estão na diago-nal secundária.


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

print(secundaria(M))
print(secundaria(M2))
print(secundaria(M3))
print(secundaria(M4))