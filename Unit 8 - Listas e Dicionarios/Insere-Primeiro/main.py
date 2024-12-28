def insere_ordenado_primeiro(l1):
    base = l1[0]
    controle = 0
    for i in range(1, len(l1)):
        if base > l1[i]:
            l1[controle], l1[i] = l1[i], l1[controle]
            controle += 1


l1 = [5, 2, 6, 9, 11, 13]
insere_ordenado_primeiro(l1)
assert l1 == [2, 5, 6, 9, 11, 13]

l2 = [3, 1, 2, 4]
insere_ordenado_primeiro(l2)
assert l2 == [1, 2, 3, 4]

l2 = [5, 1, 2, 3, 4, 5]
insere_ordenado_primeiro(l2)
assert l2 == [1, 2, 3, 4, 5, 5]
