def matriz(m):
    unidimensional = []

    for i in range(len(m[0])):
        soma = 0
        for j in range(len(m)):
            soma += m[j][i]
        unidimensional.append(soma)

    return unidimensional


"""
Faça um programa que permita ao usuário entrar com uma matriz de 3 x 3 números
inteiros. Em seguida, gere um array unidimensional pela soma dos números de cada
coluna da matriz e mostrar na tela esse array. Por exemplo, a matriz:
5 -8 10
1 2 15
25 10 7
Vai gerar um vetor, onde cada posição é a soma das colunas da matriz. A primeira
posição será 5 + 1 + 25, e assim por diante:
31 4
3
"""

m = [[5,-8,10],[1,2,15],[25,10,7]]

print(matriz(m))