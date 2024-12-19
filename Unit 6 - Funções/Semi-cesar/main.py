def dentro(letra, alfabeto):
    for i in range(len(alfabeto)):
        if letra == alfabeto[i]:
            return True
    return False


def inde(letra, alfabeto):
    indice = 0
    for i in range(len(alfabeto)):
        if letra == alfabeto[i]:
            return indice
        indice += 1


def cesar(msg, d):
    alfabeto = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]

    palavra = ""

    for i in range(len(msg)):
        if dentro(msg[i], alfabeto):
            posicao = inde(msg[i], alfabeto)
            if (posicao + d) > 26:
                posicao = (posicao + d)%26
                palavra += str(alfabeto[posicao])
            else:
                palavra += str(alfabeto[posicao + d])
        else:
            palavra += msg[i]

    return palavra


assert cesar("exemplo", 4) == "ibiqtps"
assert cesar("Exemplo 2!", 4) == "Ebiqtps 2!"
assert cesar("Exemplo1, Exemplo2", 4) == "Ebiqtps1, Ebiqtps2"
assert cesar("Exemplo1, Exemplo2", 56) == "Ebiqtps1, Ebiqtps2"
assert cesar("Exemplo1, Exemplo2", 0) == "Exemplo1, Exemplo2"
assert cesar('casa', 1) == 'dbtb'
assert cesar('casa', 2) == 'ecuc'
assert cesar('Zebra', 2) == 'Bgdtc'




