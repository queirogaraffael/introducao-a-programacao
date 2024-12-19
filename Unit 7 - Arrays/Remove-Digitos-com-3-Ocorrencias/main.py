def contador(numero, lista):
    contador = 0
    for i in range(len(lista)):
        if lista[i] == numero:
            contador += 1
    return contador


def triplets(lista):
    ocorrencias = []
    for i in range(0, 10):
        repeticoes = contador(i, lista)
        if repeticoes == 3:
            ocorrencias.append(i)
            
    for i in range(len(ocorrencias)):
        for j in range(len(lista) - 1, -1, -1):
            if lista[j] == ocorrencias[i]:
                lista.pop(j)
    return None


digitos = [1, 1, 2, 2, 5, 1]
assert triplets(digitos) == None
assert digitos == [2, 2, 5]

digitos = [1, 2, 1, 2, 1, 1]
assert triplets(digitos) == None
assert digitos == [1, 2, 1, 2, 1, 1]

digitos = [1, 2, 1, 2, 1, 2]
assert triplets(digitos) == None
assert digitos == []
