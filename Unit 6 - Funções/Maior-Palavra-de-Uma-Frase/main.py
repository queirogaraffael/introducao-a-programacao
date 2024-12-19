def maior_palavra(palavra):
    contador, contador_antigo = 0, 0
    posicao_final = 0
    resultado = ""

    for i in range(len(palavra)):
        if palavra[i] == " ":
            if contador >= contador_antigo:
                contador_antigo = contador
                posicao_final = i
            contador = 0
        else:
            contador += 1

    if contador >= contador_antigo:
        contador_antigo = contador
        posicao_final = len(palavra)

    posicao_inicial = posicao_final - contador_antigo

    for i in range(posicao_inicial, posicao_final):
        resultado += palavra[i]

    return resultado


assert maior_palavra("eu acredito que seja um bom exemplo") == "acredito"
assert maior_palavra("eu exemplo que seja um bom acredito") == "acredito"
assert maior_palavra("acredito eu que seja um bom exemplo") == "acredito"
assert maior_palavra("eu que exemplo seja um bom") == "exemplo"
assert maior_palavra("eu acredito que seja um bom exemploo") == "exemploo"
assert maior_palavra("acredito que seja um bom exemploo") == "exemploo"
