def scroll(m):
    if len(m) == 0:
        return []
    else:
        tamanho = len(m[0])
        m.pop(0)
        apoio = []

        for i in range(tamanho):
            apoio.append(0)

        m.append(apoio)

        return m


m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16],
     [17, 18, 19, 20]]

scroll(m)
assert m == [[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20],
             [0, 0, 0, 0]]

m = [[1, 2, 3, 4]]
scroll(m)
assert m == [[0, 0, 0, 0]]

m = []
scroll(m)
assert m == []
