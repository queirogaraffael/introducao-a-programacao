def dentro(num, lista):
    for i in range(len(lista)):
        if num == lista[i]:
            return True
    return False


def lista_so_com_oposto(lista):
    opostos = []

    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] + lista[j] == 0:
                opostos.append(lista[i])
                break

    for i in range(len(lista) - 1, -1, -1):
        if not dentro(lista[i], opostos):
            lista.pop(i)

    return None


lista1 = [1, 2, 1, 3, 4, -1, -3, 5]
assert lista_so_com_oposto(lista1) == None
assert lista1 == [1, 1, 3, -1, -3]

lista1 = [1, 2, 3, 4, -1, -3, 5, -5]
assert lista_so_com_oposto(lista1) == None
assert lista1 == [1, 3, -1, -3, 5, -5]

lista1 = [1, 2, 3, 4, 5, 6]
assert lista_so_com_oposto(lista1) == None
assert lista1 == []
