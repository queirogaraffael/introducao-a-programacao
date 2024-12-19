def filtra_divisores(lista):
    for i in range(len(lista) - 1, -1, -1):
        soma = 0
        numero = list(str(lista[i]))

        for j in range(len(numero)):
            soma += int(numero[j])

        if lista[i] % soma != 0:
            lista.pop(i)
    return None


lista1 = [333, 121, 81]
assert filtra_divisores(lista1) == None
assert lista1 == [333, 81]

lista1 = [121, 121, 121]
assert filtra_divisores(lista1) == None
assert lista1 == []

lista1 = [333, 121, 9, 15, 21]
assert filtra_divisores(lista1) == None
assert lista1 == [333, 9, 21]

lista1 = [121, 121, 121, 177, 177]
assert filtra_divisores(lista1) == None
assert lista1 == []