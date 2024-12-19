def remove_divisores_k(lista, k, n):
    removidos = 0
    for i in range(len(lista) - 1, -1, -1):
        if removidos == n:
            break
        if k % lista[i] == 0:
            lista.pop(i)
            removidos += 1
    


l1 = [8, 1, 2, 2, 13, 4, 19]
remove_divisores_k(l1, 4, 2)
assert l1 == [8, 1, 2, 13, 19]

l1 = [8, 1, 2, 2, 13, 4, 19]
remove_divisores_k(l1, 4, 4)
assert l1 == [8, 13, 19]

l1 = [8, 1, 2, 2, 13, 4, 19]
remove_divisores_k(l1, 4, 6)
assert l1 == [8, 13, 19]

l1 = [8, 1, 2, 2, 13, 4, 19]
remove_divisores_k(l1, 4, 0)
assert l1 == [8, 1, 2, 2, 13, 4, 19]


