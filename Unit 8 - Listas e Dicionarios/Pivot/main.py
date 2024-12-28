def pivot(numeros):
    pivot = numeros[0]
    trocas = 1

    for i in range(1, len(numeros)):
        if pivot > numeros[i]:
            for j in range(i, i - trocas, -1):
                numeros[j], numeros[j - 1] = numeros[j - 1], numeros[j]
        else:
            trocas += 1


numeros = [6, 4, 8, 1, 7, 3]
pivot(numeros)
assert numeros == [4, 1, 3, 6, 8, 7]

numeros = [5, 1, 2, 3, 7, 8, 9]
pivot(numeros)
assert numeros == [1, 2, 3, 5, 7, 8, 9]

numeros = [1, -1, -2, 7, 8]
pivot(numeros)
assert numeros == [-1, -2, 1, 7, 8]

numeros = [0, -1, -2, 1, 2]
pivot(numeros)
assert numeros == [-1, -2, 0, 1, 2]

numeros = [0, -1, 0, 1, 2, -2]
pivot(numeros)
assert numeros == [-1, -2, 0, 0, 1, 2]

numeros = [0, 0, -1, 1, 2, -2]
pivot(numeros)
assert numeros == [-1, -2, 0, 0, 1, 2]



numeros = [0, -1, -2, 1, 0, 2]
pivot(numeros)
assert numeros == [-1, -2, 0, 0, 1, 2]

numeros = [0, -1, -2, 1, 2, 0]
pivot(numeros)
assert numeros == [-1, -2, 0, 0, 1, 2]
