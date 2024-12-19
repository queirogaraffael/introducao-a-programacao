def bubble_sort(lista):
    for i in range(len(lista)-1):
      for j in range(len(lista)-1-i):
        if lista[j]<lista[j+1]:
          lista[j], lista[j+1] = lista[j+1], lista[j]

lista = [2,4,2,6,0]

bubble_sort(lista)
print(lista)