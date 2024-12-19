def dentro(num, lista):
    for i in range(len(lista)):
        if num == lista[i]:
            return True
    return False


def acordes(musica_1, musica_2):
    nova_lista = []

    for i in range(len(musica_1)):
        nova_lista.append(musica_1[i])

    for i in range(len(musica_2)):
        if not dentro(musica_2[i], musica_1):
            nova_lista.append(musica_2[i])

    return nova_lista


m1 = ['c', 'd', 'dm']
m2 = ['c', 'a']
assert acordes(m1, m2) == ['c', 'd', 'dm', 'a']
assert m1 == ['c', 'd', 'dm']
assert m2 == ['c', 'a']

m1 = ['c', 'd']
m2 = ['c', 'a']
assert acordes(m1, m2) == ['c', 'd', 'a']

m1 = ['c', 'd']
m2 = ['c', 'd']
assert acordes(m1, m2) == ['c', 'd']