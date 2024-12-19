def altera_posicao(posicao,lista):
  for i in range(len(lista)-1,posicao,-1):
    lista[i], lista[i-1] = lista[i-1], lista[i] 


def na_posicao(lista, a_inserir):
  for i in range(len(a_inserir)):
    lista.append(a_inserir[i][0])
    altera_posicao(a_inserir[i][1],lista)

  return None


l = [10, 20, 30]
a_inserir = [(5, 1), (-2, 4), (0, 0)]
assert na_posicao(l, a_inserir) == None
assert l == [0, 10, 5, 20, 30, -2]

l = [10, 20, 30]
a_inserir = [(5, 1), (-2, 4), (0, 0), (23,0),(50,7), (13,7), (22,5), (10,10)]
assert na_posicao(l, a_inserir) == None
assert l == [23, 0, 10, 5, 20, 22, 30, -2,13, 50,10]