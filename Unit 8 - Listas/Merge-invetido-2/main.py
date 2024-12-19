def merge_invertido(lista1, lista2):   
    i = len(lista1) - 1
    j = len(lista2) - 1
    merge = []
    
    while True:
        if i < 0 or j < 0: break
        if lista1[i] > lista2[j]:
            maior = lista1[i]
            i -= 1
        else:
            maior = lista2[j]
            j -= 1
        merge.append(maior)

    if i >= 0:
      for k in range(i,-1,-1):
        merge.append(lista1[k])
    
    if j >= 0:
      for z in range(j,-1,-1):
        merge.append(lista2[z])

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





  
 