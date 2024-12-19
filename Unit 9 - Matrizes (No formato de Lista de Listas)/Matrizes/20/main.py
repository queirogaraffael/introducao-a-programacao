def som_c_impares(m):
    soma = 0

    for i in range(len(m)):
        for j in range(len(m[0])):
            if j % 2 != 0:
                soma += m[i][j]


def media(m):
    soma = 0
    contador = 0

    for i in range(len(m)):
        for j in range(len(m[0])):
            if j == 1 or j == 3:
                soma += m[i][j]
                contador += 1

    media = soma / (len(m)*2)
    return media


def substituicao(m):
    matriz = []

    for i in range(len(m)):
        soma = 0
        for j in range(2):
          soma += m[i][j]
        matriz.append(soma)

    print(matriz)

    for i in range(len(m)):
        m[i][5] = matriz[i]
      
    return m

          

"""
20. Faça programa que leia uma matriz 3 x 6 com valores reais.
(a) Imprima a soma de todos os elementos das colunas ı́mpares.
(b) Imprima a média aritmética dos elementos da segunda e quarta colunas.
(c) Substitua os valores da sexta coluna pela soma dos valores das colunas 1 e 2.
(d) Imprima a matriz modificada.

"""

m = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]

print(substituicao(m))