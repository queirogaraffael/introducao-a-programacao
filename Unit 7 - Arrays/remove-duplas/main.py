#prog1
# UFCG - computação
# Raffael queiroga
# Data: 06/10/2021
# prova 3
# Recebe uma lista de interios e remove dessa lista os elementos
# que aparecerem duas vezes.


def contador(numero, lista):
    contador = 0
    for i in range(len(lista)):
        if lista[i] == numero:
            contador += 1
    return contador


def dentro(valor, lista):
    for i in range(len(lista)):
        if valor == lista[i]:
            return True
    return False


def remove_duplas(lista):
    ocorrencias = []
    for i in range(len(lista)):
        repeticoes = contador(lista[i], lista)
        if repeticoes == 2:
            if not dentro(lista[i], ocorrencias):
                ocorrencias.append(lista[i])

    for i in range(len(lista) - 1, -1, -1):
        if dentro(lista[i], ocorrencias):
            lista.pop(i)
    return None



lista = [1, 1, 20, 20, 5, 1]
assert remove_duplas(lista) == None
assert lista == [1, 1, 5, 1]

lista = [-10, 12, -10, 12, -10, -10]
assert remove_duplas(lista) == None
assert lista == [-10, -10, -10, -10]

lista = [1, 20, 20, 5, 1]
assert remove_duplas(lista) == None
assert lista == [5]

lista = [-10, 12, 12, -10]
assert remove_duplas(lista) == None
assert lista == []

lista = [-11, 12, -13, 14, -15, -16]
assert remove_duplas(lista) == None
assert lista == [-11, 12, -13, 14, -15, -16]
