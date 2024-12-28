def filtra_lista(num, numeros):
    lista = []
    for i in range(len(numeros)):
        if i % num == 0:
            lista.append(numeros[i])
    return lista


numeros1 = [0, 1, 2, 3, 4, 5, 6]
assert filtra_lista(2, numeros1) == [0, 2, 4, 6]
assert filtra_lista(3, numeros1) == [0, 3, 6]

numeros2 = [2, 3, 5, 7, 11, 13, 17]
assert filtra_lista(4, numeros2) == [2, 11]
assert filtra_lista(40, numeros2) == [2]
