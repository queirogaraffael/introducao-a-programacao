def insere_ordenado_impostor(lista):
    valor = 0

    for i in range(len(lista) - 1, 0, -1):
        if lista[i] < lista[i - 1]:
            valor = lista[i]
            lista.pop(i)
            break
    lista.append(valor)

    for i in range(len(lista) - 1, 0, -1):
        if lista[i] < lista[i - 1]:
            lista[i], lista[i - 1] = lista[i - 1], lista[i]
        else:
            break


l = [1, 2, 4, 3, 5, 6, 7, 11]
insere_ordenado_impostor(l)
assert l == [1, 2, 3, 4, 5, 6, 7, 11]

l = [1, 0, 3, 4, 5, 6, 7, 11]
insere_ordenado_impostor(l)
assert l == [0, 1, 3, 4, 5, 6, 7, 11]

l = [1, 9, 11, 3, 14]
insere_ordenado_impostor(l)
assert l == [1, 3, 9, 11, 14]

l = [1, 8, 9, 11, 15, 14]
insere_ordenado_impostor(l)
assert l == [1, 8, 9, 11, 14, 15]

l = [1, 2, 3, 4, 6, 15, 7, 16]
insere_ordenado_impostor(l)
assert l == [1, 2, 3, 4, 6, 7, 15, 16]

l = [1, 2, 3, 4, 6, 7, 15, 16, 0]
insere_ordenado_impostor(l)
assert l == [0, 1, 2, 3, 4, 6, 7, 15, 16]
