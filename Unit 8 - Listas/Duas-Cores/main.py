def separa_duas_cores(lista, cor1, cor2):
    indices = []

    for i in range(len(lista)):
        if lista[i] == cor1:
            indices.append(i)

    for i in range(len(indices)):
        lista[i], lista[indices[i]] = lista[indices[i]], lista[i]

    return None


l1 = ['a', 'a', 'b', 'a', 'b']
assert separa_duas_cores(l1, 'b', 'a') == None
assert l1 == ['b', 'b', 'a', 'a', 'a']

l1 = ['a', 'a', 'b', 'a', 'b']
assert separa_duas_cores(l1, 'a', 'b') == None
assert l1 == ['a', 'a', 'a', 'b', 'b']

l1 = ['a', 'b', 'a', 'a', 'b']
assert separa_duas_cores(l1, 'a', 'b') == None
assert l1 == ['a', 'a', 'a', 'b', 'b']

l1 = ['b', 'a', 'b', 'a', 'b']
assert separa_duas_cores(l1, 'b', 'a') == None
assert l1 == ['b', 'b', 'b', 'a', 'a']

l1 = ['b', 'b', 'b', 'b', 'a']
assert separa_duas_cores(l1, 'a', 'b') == None
assert l1 == ['a', 'b', 'b', 'b', 'b']

l1 = ['a', 'b', 'b', 'b', 'b']
assert separa_duas_cores(l1, 'a', 'b') == None
assert l1 == ['a', 'b', 'b', 'b', 'b']