def soma_diminui_vizinhos(lista):
  valor = 0
  if lista == []:
    return valor
  else:
    for i in range(len(lista)):
        if i == 0 or i == 1 or i % 2 != 0:
            valor += int(lista[i])
        else:
            valor -= int(lista[i])
    return valor


lista = [1, 2, 3]
assert soma_diminui_vizinhos(lista) == 0

lista = [1, 2, 3, 4]
assert soma_diminui_vizinhos(lista) == 4

lista = [1, 2, 3, 4, 5]
assert soma_diminui_vizinhos(lista) == -1

lista = [1, 2, 3, 4, 5, 6]
assert soma_diminui_vizinhos(lista) == 5

lista = [1, 2, 3, 4, 5, 6, 7]
assert soma_diminui_vizinhos(lista) == -2

lista = [1, 2, 3, 4, 5, 6, 7, 8]
assert soma_diminui_vizinhos(lista) == 6

lista = [1, 2]
assert soma_diminui_vizinhos(lista) == 3

lista = []
assert soma_diminui_vizinhos(lista) == 0

lista = [0, 0]
assert soma_diminui_vizinhos(lista) == 0

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
assert soma_diminui_vizinhos(lista) == 12

lista = [-1, -4, -5]
assert soma_diminui_vizinhos(lista) == 0

lista = [1]
assert soma_diminui_vizinhos(lista) == 1