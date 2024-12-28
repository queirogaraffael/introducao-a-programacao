def contador(nome, lista):
    contador = 0

    for i in range(len(lista)):
        if nome == lista[i]:
            contador += 1

    return contador


def lanchemaispedido(lista):
    metade = len(lista) / 2

    for i in range(len(lista)):
        x = contador(lista[i], lista)
        if x > metade:
            return lista[i]

    return None


ines = ['tapioca', 'tapioca', 'salada', 'bolo', 'misto', 'tapioca', 'tapioca']
marcos = ['suco', 'coxinha', 'suco', 'misto', 'folhado']
lista1 = ['tapioca', 'tapioca', 'salada', 'bolo', 'misto', 'tapioca', 'tapiocaa']


assert lanchemaispedido(ines) == 'tapioca'
assert lanchemaispedido(marcos) == None
assert lanchemaispedido(lista1) == None

