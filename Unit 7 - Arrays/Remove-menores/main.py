def remove_menores(N, lista):
    eliminados = 0

    for i in range(len(lista) - 1, -1, -1):
        if lista[i] < N:
            lista.pop(i)
            eliminados += 1

    return eliminados


lista = [1, 2, 3, 4, 5]
assert remove_menores(3, lista) == 2
assert lista == [3, 4, 5]

lista = [1, 2, 3, 4, 5]
assert remove_menores(5, lista) == 4
assert lista == [5]