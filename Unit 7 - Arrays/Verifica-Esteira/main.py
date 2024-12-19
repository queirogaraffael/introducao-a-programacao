def dentro(num, lista):
    for i in range(len(lista)):
        if num == lista[i]:
            return True
    return False


def dentro2(lista1, lista2):
    for i in range(len(lista2)):
        if not dentro(lista2[i], lista1):
            return False
    return True


def dentro3(nova_lista, componentes):
    for i in range(len(nova_lista) - len(componentes) + 1):
        controle = i
        controle2 = 0
        for j in range(len(componentes)):
            if nova_lista[controle] == componentes[j]:
                controle += 1
                controle2 += 1
                if controle2 == len(componentes):
                    return True
    return False


def verifica_esteira(esteira, componentes):
    if dentro2(esteira, componentes):
        nova_lista = []
        for i in range(len(esteira)):
            if dentro(esteira[i], componentes):
                nova_lista.append(esteira[i])
        if dentro3(nova_lista, componentes):
            return True
    return False


esteira = [2, 1, 3, 4]
componentes = [2, 4]
assert verifica_esteira(esteira, componentes) == True
assert esteira == [2, 1, 3, 4]
assert componentes == [2, 4]

esteira = [1, 3, 4]
componentes = [4, 1, 3]
assert not verifica_esteira(esteira, componentes) == True
assert esteira == [1, 3, 4]
assert componentes == [4, 1, 3]

esteira = [2, 1, 3, 4]
componentes = [2, 4, 1]
assert verifica_esteira(esteira, componentes) == False
assert esteira == [2, 1, 3, 4]
assert componentes == [2, 4, 1]

esteira = [2, 2, 1, 3, 4]
componentes = [2, 2, 4]
assert verifica_esteira(esteira, componentes) == True
assert esteira == [2, 2, 1, 3, 4]
assert componentes == [2, 2, 4]

esteira = [2, 2, 4, 1, 3, 4]
componentes = [2, 2, 4]
assert verifica_esteira(esteira, componentes) == True
assert esteira == [2, 2, 4, 1, 3, 4]
assert componentes == [2, 2, 4]

esteira = [2, 2, 2, 1, 3, 4]
componentes = [2, 2, 4]
assert verifica_esteira(esteira, componentes) == True
assert esteira == [2, 2, 2, 1, 3, 4]
assert componentes == [2, 2, 4]

esteira = [4, 2, 2, 1, 3, 4]
componentes = [2, 2, 4]
assert verifica_esteira(esteira, componentes) == True
assert esteira == [4, 2, 2, 1, 3, 4]
assert componentes == [2, 2, 4]

esteira = [2, 2, 2, 4, 3, 4]
componentes = [2, 2, 4]
assert verifica_esteira(esteira, componentes) == True
assert esteira == [2, 2, 2, 4, 3, 4]
assert componentes == [2, 2, 4]

esteira = [2, 4, 2, 2, 4, 3, 4]
componentes = [2, 2, 4]
assert verifica_esteira(esteira, componentes) == True
assert esteira == [2, 4, 2, 2, 4, 3, 4]
assert componentes == [2, 2, 4]

esteira = [2, 4, 2, 2, 2, 2, 4]
componentes = [2, 2, 2, 4]
assert verifica_esteira(esteira, componentes) == True
assert esteira == [2, 4, 2, 2, 2, 2, 4]
assert componentes == [2, 2, 2, 4]