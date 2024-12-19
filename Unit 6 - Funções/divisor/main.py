def divisor(num, lista):
    for i in range(len(lista)):
      if lista[i]%num==0:
        return i
    return -1


lista1 = [10,10,40,50]
lista2 = [3,15,50,23,5]
assert divisor(3, lista1) == -1
assert divisor(5, lista2) == 1