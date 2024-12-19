def ordena(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - i - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def noves_fora(valor):
    nova_lista = []
    if len(valor) == 1:
        if valor[0] == 9:
            nova_lista.append([9])
            nova_lista.append([0])
            return 0, nova_lista
        elif 0 < (valor[0] - 9) < 9:
            soma = valor[0] - 9
            nova_lista.append(valor[:])
            nova_lista.append([soma])
            return soma, nova_lista
        else:
            soma = valor[0]
            nova_lista.append(valor[:])
            return soma, nova_lista
    else:
        nova_lista = []
        for i in range(len(valor) - 1):
            nova_lista.append(valor[:])

            numero1, numero2 = valor[0], valor[1]
            valor.pop(0)
            valor.pop(0)

            if 0 <= (numero1 + numero2 - 9) < 9:
                soma = numero1 + numero2 - 9
            elif (numero1 + numero2 - 9) == 9:
                soma = 0
            else:
                soma = numero1 + numero2

            valor.append(soma)
            ordena(valor)
        nova_lista.append(valor[:])
        return int(valor[0]), nova_lista


assert noves_fora([9, 7, 5, 4, 3, 1]) == (2, [[9, 7, 5, 4, 3, 1],
                                              [7, 5, 4, 3, 1], [4, 3, 3, 1],
                                              [7, 3, 1], [1, 1], [2]])
assert noves_fora([9, 8, 7, 7, 6, 5, 4, 2]) == (3, [[9, 8, 7, 7, 6, 5, 4, 2],
                                                    [8, 7, 7, 6, 5, 4, 2],
                                                    [7, 6, 6, 5, 4, 2],
                                                    [6, 5, 4, 4, 2],
                                                    [4, 4, 2, 2], [8, 2, 2],
                                                    [2, 1], [3]])
assert noves_fora([9, 9]) == (0, [[9, 9], [0]])
assert noves_fora([7, 5, 4, 3, 1]) == (2, [[7, 5, 4, 3, 1], [4, 3, 3, 1],
                                           [7, 3, 1], [1, 1], [2]])

assert noves_fora([8, 7, 7, 6, 5, 4, 2]) == (3, [[8, 7, 7, 6, 5, 4, 2],
                                                 [7, 6, 6, 5, 4, 2],
                                                 [6, 5, 4, 4, 2], [4, 4, 2, 2],
                                                 [8, 2, 2], [2, 1], [3]])

assert noves_fora([9, 9, 9, 9]) == (0, [[9, 9, 9, 9], [9, 9, 0], [0, 0],
                                        [0]])  # analisar mais
assert noves_fora([9, 9, 9]) == (0, [[9, 9, 9], [9, 0], [0]])  # analisar mais

assert noves_fora([4, 4]) == (8, [[4, 4], [8]])
assert noves_fora([4, 4, 4]) == (3, [[4, 4, 4], [8, 4], [3]])

assert noves_fora([5, 4]) == (0, [[5, 4], [0]])
assert noves_fora([9]) == (0, [[9], [0]])

assert noves_fora([10]) == (1, [[10], [1]])

assert noves_fora([4]) == (4, [[4]])

assert noves_fora([8]) == (8, [[8]])

assert noves_fora([4, 4]) == (8, [[4, 4], [8]])