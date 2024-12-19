def remove(lista,numero):
    for i in range(len(lista)-1, -1, -1):
        if lista[i] == numero:
            lista.pop(i)
    return lista


lista = [10, 20, 20, 20, 30, 50]

print(remove(lista,20))

