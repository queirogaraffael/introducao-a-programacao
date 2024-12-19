def conta_palavras(k, palavras):
    lista = palavras.split(":")
    contador = 0

    for i in range(len(lista)):
        if len(lista[i]) >= k:
            contador += 1

    return contador


assert conta_palavras(5, "zero:um:dois:tres:quatro:cinco") == 2

assert conta_palavras(0, "zero:um:dois:tres:quatro:cinco") == 6
