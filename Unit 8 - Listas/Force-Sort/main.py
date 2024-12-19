def force_sort(seq):
    if len(seq) == 0:
        return []
    else:
        diferencas = [0]

        for i in range(1, len(seq)):
            if seq[i] < seq[i - 1]:
                dif = abs(seq[i] - seq[i - 1])
                seq[i] = seq[i - 1]
                diferencas.append(dif)
            else:
                diferencas.append(0)
        return diferencas


seq = [1, 3, 5, 4, 9]
assert force_sort(seq) == [0, 0, 0, 1, 0]
assert seq == [1, 3, 5, 5, 9]

seq = [1, 3, 5, 4, 9, 2, 15]
assert force_sort(seq) == [0, 0, 0, 1, 0, 7, 0]
assert seq == [1, 3, 5, 5, 9, 9, 15]

seq = [3, 1, 5, 4, 9]
assert force_sort(seq) == [0, 2, 0, 1, 0]
assert seq == [3, 3, 5, 5, 9]

seq = [3, 1]
assert force_sort(seq) == [0, 2]
assert seq == [3, 3]

seq = [1, 3]
assert force_sort(seq) == [0, 0]
assert seq == [1, 3]

seq = []
assert force_sort(seq) == []
assert seq == []

seq = [1]
assert force_sort(seq) == [0]
assert seq == [1]
