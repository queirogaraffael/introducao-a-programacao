def removedor(num, lista):
    for i in range(len(lista) - 1, -1, -1):
        if num == lista[i]:
            lista.pop(i)
            break


def organiza_por_media(lista):
    if lista == []:
        return []
    else:
        soma = 0
        auxiliar = []

        for i in range(len(lista)):
            soma += lista[i]

        media = soma / len(lista)

        for i in range(len(lista)):
            if lista[i] > media:
                auxiliar.append(lista[i])

        for i in range(len(auxiliar)):
            removedor(auxiliar[i], lista)

        for i in range(len(auxiliar)):
            lista.append(auxiliar[i])

        return lista


p1 = [1, 2, 4, 1, 3, 4, 56, 7, 7, 4, 3, 67]
assert organiza_por_media(p1) == [1, 2, 4, 1, 3, 4, 7, 7, 4, 3, 56, 67]
assert p1 == [1, 2, 4, 1, 3, 4, 7, 7, 4, 3, 56, 67]

p1 = [1, 2, 4, 1, 3, 4, 56, 50, 7, 4, 3, 67]
assert organiza_por_media(p1) == [1, 2, 4, 1, 3, 4, 7, 4, 3, 56, 50, 67]
assert p1 == [1, 2, 4, 1, 3, 4, 7, 4, 3, 56, 50, 67]

p1 = [1, 2, 4, 1, 3, 50, 56, 50, 7, 4, 3, 67]
assert organiza_por_media(p1) == [1, 2, 4, 1, 3, 7, 4, 3, 50, 56, 50, 67]
assert p1 == [1, 2, 4, 1, 3, 7, 4, 3, 50, 56, 50, 67]

p1 = []
assert organiza_por_media(p1) == []
assert p1 == []

p1 = [1]
assert organiza_por_media(p1) == [1]
assert p1 == [1]