def flip(array, i, j):
    repeticoes = (j - i) // 2
    for k in range(repeticoes + 1):
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    return None


array = [1, 2, 3, 4, 5, 6, 7]
assert flip(array, 2, 5) == None
assert array == [1, 2, 6, 5, 4, 3, 7]

array = [1, 2, 3, 4, 5, 6, 7]
assert flip(array, 0, 3) == None
assert array == [4, 3, 2, 1, 5, 6, 7]

array = [1, 2, 3, 4, 5, 6, 7]
assert flip(array, 3, 6) == None
assert array == [1, 2, 3, 7, 6, 5, 4]

array = [1, 2, 3, 4, 5, 6, 7]
assert flip(array, 2, 3) == None
assert array == [1, 2, 4, 3, 5, 6, 7]

array = [1, 2, 3, 4, 5, 6, 7]
assert flip(array, 2, 2) == None
assert array == [1, 2, 3, 4, 5, 6, 7]

array = [1, 2, 3, 4, 5, 6, 7]
assert flip(array, 0, 6) == None
assert array == [7, 6, 5, 4, 3, 2, 1]

array = [1, 2, 3, 4, 5, 6, 7, 8]
assert flip(array, 0, 7) == None
assert array == [8, 7, 6, 5, 4, 3, 2, 1]

array = [1, 2, 3, 4, 5, 6, 7]
assert flip(array, 0, 2) == None
assert array == [3, 2, 1, 4, 5, 6, 7]
