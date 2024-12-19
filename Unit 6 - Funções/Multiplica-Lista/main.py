def multiplica_lista(n, lista):
    nova_lista = []
    if n == 0:
        return nova_lista
    else:
        controle = n
        while True:
            for i in range(len(lista)):
                nova_lista.append(lista[i])
            if controle <= 1: break
            controle -= 1

        return nova_lista


l = ['joao', 'pedro']
print(l)
assert multiplica_lista(4, l) == [
    'joao', 'pedro', 'joao', 'pedro', 'joao', 'pedro', 'joao', 'pedro'
]
print(l)

l1 = ["ola", "oii"]
assert multiplica_lista(3, l1) == ["ola", "oii", "ola", "oii","ola", "oii"]

l2 = [2, 2, 3, "3"]
assert multiplica_lista(1, l2) == [2, 2, 3, "3"]

l5 = ['joao', 'pedro', 'joao', 'pedro']
assert multiplica_lista(0, l5) == []

print(l1)
print(l2)
print(l5)

assert multiplica_lista(8, l) == [
    'joao', 'pedro', 'joao', 'pedro', 'joao', 'pedro', 'joao', 'pedro', 'joao',
    'pedro', 'joao', 'pedro', 'joao', 'pedro', 'joao', 'pedro'
]
