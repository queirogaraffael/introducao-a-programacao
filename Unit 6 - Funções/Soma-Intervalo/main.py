def soma_intervalo(a, b):
    numero1 = a
    soma = 0
    while True:
        soma += numero1
        if numero1 == b: break
        numero1 += 1
    return soma


assert soma_intervalo(5, 15) == 110
assert soma_intervalo(10, 10) == 10
