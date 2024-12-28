def busca(lista, num):
    indice = 0
    for i in range(len(lista)):
        if num == lista[i]:
            return indice
        indice += 1
    return -1


seq = [8, 9, 2, 3, 6, 10, 7, 9]
assert busca(seq, 6) == 4
assert busca(seq, 4) == -1
assert busca(seq, 9) == 1
assert busca(seq, 8) == 0