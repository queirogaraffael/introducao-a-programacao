def eh_primo(numero):
    controle = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            controle += 1
    if controle == 2:
        return True
    else:
        return False


def primos_ate(limite):
    valores = []
    for i in range(1, limite):
        if eh_primo(i):
            valores.append(i)
    return valores


assert primos_ate(10) == [2, 3, 5, 7]
assert primos_ate(29) == [2, 3, 5, 7, 11, 13, 17, 19, 23]
