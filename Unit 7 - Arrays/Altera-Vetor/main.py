def altera_vetor_por_escalar(vetor, num):
    for i in range(len(vetor)):
        vetor[i] = vetor[i] * num
    return None


vetor_1 = [1, 2, 3]
assert altera_vetor_por_escalar(vetor_1, -1) == None
assert vetor_1 == [-1, -2, -3]
assert altera_vetor_por_escalar(vetor_1, 2) == None
assert vetor_1 == [-2, -4, -6]
assert altera_vetor_por_escalar(vetor_1, 0) == None
assert vetor_1 == [0, 0, 0]
