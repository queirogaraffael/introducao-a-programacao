def inverte3a3(s):
    lista_dividida, nova_lista = [], []
    controle = 0
    nome = ""

    for i in s:
        if controle <= 3:
            nome += i
            controle += 1
            if controle == 3:
                lista_dividida.append(nome)
                controle = 0
                nome = ""

    for i in range(-1, -len(lista_dividida) - 1, -1):
        nova_lista.append(lista_dividida[i])

    nome_final = "".join(nova_lista)

    return nome_final


assert inverte3a3("abcdef") == "defabc"

assert inverte3a3("abcdefghijkl") == "jklghidefabc"

assert inverte3a3("abc") == "abc"
