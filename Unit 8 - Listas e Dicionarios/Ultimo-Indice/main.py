def dentro(num, lista):
    for i in range(len(lista)):
        if num == lista[i]:
            return True
    return False


def ultimo_indice(num, lista):
    if not dentro(num, lista):
        return -1
    else:
        indice = 0
        for i in range(len(lista)):
            if lista[i] == num:
                indice = i
        return indice


assert ultimo_indice(0, [0, 2, 15, 11, 14, 2]) == 0
assert ultimo_indice(0, [15, 2, 0, 11, 14, 2]) == 2
assert ultimo_indice(0, [15, 2, 13, 11, 14, 2]) == -1
assert ultimo_indice(2, [15, 2, 13, 11, 14, 2]) == 5
assert ultimo_indice(42, [15, 2, 13, 11, 14, 2]) == -1
assert ultimo_indice(15, [15, 2, 13, 11, 14, 2]) == 0
