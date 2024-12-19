def caixa_alta(palavra):
    if len(palavra) == 1:
        x = palavra[0].lower()
        return x
    else:
        resultado = ""
        contador, controle, controle2 = 0, 0, 0
        for i in range(len(palavra)):
            if palavra[i] == " " or i == len(palavra) - 1:
                if i == len(palavra) - 1:
                    if palavra[i - 1] == " ":
                        controle2 = 0
                        contador = 1
                    else:
                        controle = 1 + i
                else:
                    controle = i
                    controle2 = 1
                if contador == 1:
                    x = palavra[i - controle2].lower()
                    resultado += x
                    contador = 0
                else:
                    primeira = palavra[i - contador].capitalize()
                    resultado += primeira
                    for j in range(i - contador + 1, controle):
                        resultado += palavra[j].lower()
                if not i == len(palavra) - 1:
                    resultado += " "
                contador = 0
            else:
                contador += 1
        return resultado


assert caixa_alta(
    "A primeira letra de cada palavra") == "a Primeira Letra De Cada Palavra"
assert caixa_alta(
    "a primeira letra de cada palavra") == "a Primeira Letra De Cada Palavra"
assert caixa_alta(
    "a primeira letra d cada palavra") == "a Primeira Letra d Cada Palavra"
assert caixa_alta("A primeira letra de cada P") == "a Primeira Letra De Cada p"
assert caixa_alta("primeira") == "Primeira"
assert caixa_alta("A primeira letra de p P") == "a Primeira Letra De p p"
assert caixa_alta("acaBou") == "Acabou"
assert caixa_alta("A") == "a"
assert caixa_alta("A P letra de cada palavra") == "a p Letra De Cada Palavra"
assert caixa_alta("A P letra de C P") == "a p Letra De c p"
assert caixa_alta("A P L D P") == "a p l d p"
assert caixa_alta(
    "primeira letra de cada palavra") == "Primeira Letra De Cada Palavra"
assert caixa_alta("A P") == "a p"