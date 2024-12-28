def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    nova_lista = []

    while swapped:
        swapped = False
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        if (swapped == False):
            return nova_lista

        swapped = False

        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        start = start + 1
        nova_lista.append(a)



print(print(cocktailSort([3, 4, 2, 0, 5, 6, 7,1]))
"""

print(cocktailSort([3, 4, 2, 0, 5, 6, 7,1]))

assert cocktailSort([3, 4, 2, 0, 5, 6, 7,1]) == [[3, 4, 2, 0, 5, 6, 7, 1], 
                                                 [0, 3, 2, 1, 4, 5, 6, 7], 
                                                 [0, 1, 2, 3, 4, 5, 6, 7]]

                                                 """
