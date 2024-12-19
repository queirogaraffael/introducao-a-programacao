def oculta_letras(palavra, exibir):
    resultado = ""
    palavra = list(palavra)
    exibir = list(exibir)
    for i in range(len(palavra)):
        controle = True
        for j in range(len(exibir)):
            maiscula = exibir[j].capitalize()
            minuscula = exibir[j].lower()
            if maiscula == palavra[i] or minuscula == palavra[i]:
                resultado += palavra[i]
                controle = False
                break
        if controle:
            resultado += "_"

    return resultado



assert oculta_letras("Casa", "a") == "_a_a"
assert oculta_letras("Casa", "c") == "C___"
assert oculta_letras("Casa", "aS") == "_asa"
assert oculta_letras("Casa", "Casa") == "Casa"
assert oculta_letras("CaSa", "Casa") == "CaSa"
assert oculta_letras("Casa", "casa") == "Casa"
assert oculta_letras("Casa", "asa") == "_asa"