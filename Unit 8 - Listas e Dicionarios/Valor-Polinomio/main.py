def valor_polinomio(polinomio, valor):
    expoente = 0
    soma = 0

    for i in range(len(polinomio)):
        soma += polinomio[i] * valor**expoente
        expoente += 1
    return soma


assert valor_polinomio([-5, 0, 2, 0, 3], 10) == 30195
assert valor_polinomio([-5, 0, 2, 0, 3], 2) == 51
assert valor_polinomio([-5, 0, 2, 0, 3], 0) == -5
assert valor_polinomio([3, 1], 100) == 103
assert valor_polinomio([3, 1], 8) == 11
