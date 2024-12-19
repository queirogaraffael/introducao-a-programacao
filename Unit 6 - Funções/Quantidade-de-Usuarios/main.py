def quantidade_usuarios(dicionario):
    quantidade = 0

    for chave in dicionario:
        for usuario in dicionario[chave]:
            if chave != 9999:
                quantidade += 1
    return quantidade


lsd = {1234: ['Andrey'], 1226: ['Nazareno', 'Livia'], 9999: ['administrador']}
deq = {1114: ['Ana']}

assert quantidade_usuarios(lsd) == 3
assert quantidade_usuarios(deq) == 1
