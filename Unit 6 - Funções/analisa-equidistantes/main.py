#prog1
# UFCG - computação
# Raffael queiroga
# Data: 06/10/2021
# prova 3
# O programa analisa antravés de uma lista de inteiros
# os valores equidistantes, se ambos os valores forem 
# divisiveis por 3 e por 5, o programa adiciona numa 
# lista o valor 15, se forem apenas divisiveis por 3, 
# adiciona 3 à lista, se forem # divisiveis apenas por 5, 
# adiciona 5 e se não forem divisiveis por nenhum, 
# adiciona #o produto dos valores equidistantes. 
# Caso o tamanho da lista lista seja ímpar, é acrescentado à
# lista no final do programa, o valor central. 


def analisa_equidistantes(inteiros):
    lista = []
    swap = False

    if len(inteiros) % 2 != 0:
        swap = True

    ocorrencias = len(inteiros) // 2

    for i in range(ocorrencias):
        if (inteiros[i] % 3 == 0 and inteiros[-i - 1] % 3
                == 0) and (inteiros[i] % 5 == 0 and inteiros[-i - 1] % 5 == 0):
            lista.append(15)
        elif inteiros[i] % 3 == 0 and inteiros[-i - 1] % 3 == 0:
            lista.append(3)
        elif inteiros[i] % 5 == 0 and inteiros[-i - 1] % 5 == 0:
            lista.append(5)
        else:
            produto = inteiros[i] * inteiros[-i - 1]
            lista.append(produto)
    if swap:
        lista.append(inteiros[ocorrencias])
    return lista


assert analisa_equidistantes([3, 5, 15, 2, 4, 30, 10, 6]) == [3, 5, 15, 8]
assert analisa_equidistantes([1, 9, 10, 18, 7]) == [7, 3, 10]

assert analisa_equidistantes([6, 10, 30, 4, 2, 15, 5, 3]) == [3, 5, 15, 8]
assert analisa_equidistantes([1, 2, 3, 4, 5]) == [5,8,3]

assert analisa_equidistantes([2, 3, 11, 4, 2, 2, 4, 5]) == [10, 12, 22, 8]
