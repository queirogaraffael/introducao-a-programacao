def idosos_inicio(lista):
    j = 0
    for i in range(len(lista)):
        if lista[i] >= 60:
            lista[j], lista[i] = lista[i], lista[j]
            j+=1



"""
def idosos_inicio(lista):
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[j] >= 60:
                lista[i], lista[j] = lista[j], lista[i]
                break

"""

fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
idosos_inicio(fila)
assert fila == [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]


fila2 = [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]
idosos_inicio(fila2)
assert fila2 == [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]

fila3 = [25, 33, 60, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
idosos_inicio(fila3)
assert fila3 == [60, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]