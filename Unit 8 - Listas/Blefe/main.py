def blefe(l1):
    blef = []
    if len(l1) == 0:
        return blef
    else:
        blef.append(0)
        for i in range(1, len(l1)):
            if l1[i] > l1[i - 1]:
                diferenca = abs(l1[i - 1] - l1[i])
                blef.append(diferenca)
                l1[i] = l1[i - 1]
            else:
                blef.append(0)
    return blef


l1 = [9, 4, 5, 3, 1]
assert blefe(l1) == [0, 0, 1, 0, 0]
assert l1 == [9, 4, 4, 3, 1]

l2 = [15, 9, 4, 5, 2, 1, 3, 4]
assert blefe(l2) == [0, 0, 0, 1, 0, 0, 2, 3]
assert l2 == [15, 9, 4, 4, 2, 1, 1, 1]