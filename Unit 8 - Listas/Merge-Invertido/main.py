def maior_funcao(lista):
    maior = lista[0]

    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]

    return maior


def remove(numero, lista):
    for i in range(len(lista) - 1, -1, -1):
        if numero == lista[i]:
            lista.pop(i)
            break


def merge_invertido(l1, l2):
    lista, merge = [], []

    for i in range(len(l1)):
        lista.append(l1[i])

    for i in range(len(l2)):
        lista.append(l2[i])

    for i in range(len(lista)):
        maior = maior_funcao(lista)
        merge.append(maior)
        remove(maior, lista)

    return merge


l1 = [8, 12, 78, 79, 511]
l2 = [7, 8, 121, 302]
assert merge_invertido(l1, l2) == [511, 302, 121, 79, 78, 12, 8, 8, 7]
assert l1 == [8, 12, 78, 79, 511]
assert l2 == [7, 8, 121, 302]

l1 = []
l2 = []
assert merge_invertido(l1, l2) == []
assert l1 == []
assert l2 == []

l2 = [8, 12, 78, 79, 511]
l1 = [7, 8, 121, 302]
assert merge_invertido(l1, l2) == [511, 302, 121, 79, 78, 12, 8, 8, 7]
assert l2 == [8, 12, 78, 79, 511]
assert l1 == [7, 8, 121, 302]

l2 = [8, 12, 78, 79, 511, 511, 511]
l1 = [7, 8, 121, 302]
assert merge_invertido(l1,
                       l2) == [511, 511, 511, 302, 121, 79, 78, 12, 8, 8, 7]
assert l2 == [8, 12, 78, 79, 511, 511, 511]
assert l1 == [7, 8, 121, 302]
