# Programa que soma os elementos de duas listas diferentes 
# Sua função não deve possuir efeito colateral

"""
def soma(lista1, lista2):
    soma = 0

    lista1 += lista2

    for i in lista1:
        soma += i
    return soma


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

assert soma(lista1, lista2) == 21
assert lista1 == [1, 2, 3, 4, 5, 6]
assert lista2 == [4, 5, 6]

///
def inclui(num, soma):
    num = num + soma 
    # ou num += soma, porque int é imutável
    # a ligação é cortada em NUM
    return num


num = 10
soma = 5
print(inclui(num,soma))
print(num)

///

def inclui(lista,num):

  #lista1 = lista
  #lista = lista + [num]
  #lista += [num]

  lista += [num]
  return lista


lista = [1,2,3]
print(inclui(lista,6))
print(lista)

//
def inclui(lista,num):
  lista = lista + [num]
  return lista


lista = [1,2,3]
print(inclui(lista,6))
print(lista)


////

def dobro(num):
    num = 10  #cria uma nova variáável
    return num * 2


num = 5

print(dobro(num))

print(num)
"""