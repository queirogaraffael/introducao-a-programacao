def insertion_sort(numeros):
  for i in range(1,len(numeros)):
    controle = 0
    for j in range(i-1,-1,-1):
      if numeros[i-controle] < numeros[j]:
        numeros[i-controle], numeros[j] = numeros[j], numeros[i-controle]
        controle+=1
      else:
        break


numeros = [6, 3, 7, 9, 1, 0]
insertion_sort(numeros)
assert numeros == [0, 1, 3, 6, 7, 9]

numeros = [9,8,7,6,5,4,3,2,1,0]
insertion_sort(numeros)
assert numeros == [0, 1,2,3,4,5,6,7,8,9]

numeros = [5,6,7,2,3,-1,0]
insertion_sort(numeros)
assert numeros == [-1,0,2,3,5,6,7]

numeros = [-5,-4,-3,0,1,2,3,4]
insertion_sort(numeros)
assert numeros == [-5,-4,-3,0,1,2,3,4]

numeros = [53,50,29,23,18]
insertion_sort(numeros)
assert numeros == [18,23,29,50,53]

numeros = [54,18,50,23,29]
insertion_sort(numeros)
assert numeros == [18,23,29,50,54]