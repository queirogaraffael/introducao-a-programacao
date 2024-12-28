def insere_ordenado_ultimo(lista):
    for i in range(len(lista) - 1, 0, -1):
        if lista[i] < lista[i - 1]:
            lista[i], lista[i - 1] = lista[i - 1], lista[i]
        else:
          break


l1 = [2, 6, 9, 11, 13, 5]
insere_ordenado_ultimo(l1)
assert l1 == [2, 5, 6, 9, 11, 13]

l2 = [1, 2, 3, 0]
insere_ordenado_ultimo(l2)
assert l2 == [0, 1, 2, 3]

l1 = [2, 6, 9, 11, 13, 1]
insere_ordenado_ultimo(l1)
assert l1 == [1, 2, 6, 9, 11, 13]

l1 = [2, 6, 9, 11, 13, 14, 1]
insere_ordenado_ultimo(l1)
assert l1 == [1, 2, 6, 9, 11, 13, 14]
