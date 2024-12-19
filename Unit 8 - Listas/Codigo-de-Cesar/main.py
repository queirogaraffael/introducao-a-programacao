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


def cesar(texto, delta):
    alfabeto = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]

    palavra = ""

    for i in range(len(texto)):
        letra = texto[i].lower()
        if dentro(letra, alfabeto):
            posicao = inde(letra, alfabeto)
            if (posicao + delta) >= 26:
              posicao = (posicao + delta)%26
              if texto[i].islower():
                palavra += str(alfabeto[posicao])
              else:
                palavra += str(alfabeto[posicao].upper())
            else:
              if texto[i].islower():
                palavra += str(alfabeto[posicao + delta])
              else:
                palavra += str(alfabeto[posicao + delta].upper())
        else:
            palavra += texto[i]

    return palavra


assert cesar('casa', 1) == 'dbtb'
assert cesar('casa', 2) == 'ecuc'
assert cesar('Zebra', 2) == 'Bgdtc'