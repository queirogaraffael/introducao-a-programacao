def matriz(linhas, colunas):
    resultado = []
    for i in range(linhas):
        apoio = []
        for j in range(colunas):
            if i == j:
                apoio.append(1)
            else:
                apoio.append(0)
        resultado.append(apoio)
    return resultado


#2. Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais
#elementos. Escreva ao final a matriz obtida.

print(matriz(5, 5))
print(matriz(4, 4))
print(matriz(3, 3))
