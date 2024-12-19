def dentro(nome, lista):
    for i in range(len(lista)):
        if nome == lista[i]:
            return True
    return False


def posicao_funcao(nome, lista):
    posicao = 0
    for i in range(len(lista)):
        if nome == lista[i]: break
        posicao += 1
    return posicao


def insere_nome(aluno1, duplas, aluno2):
    if not dentro(aluno2, duplas):
        duplas.append(aluno1)
    else:
        posicao = posicao_funcao(aluno2, duplas)
        duplas.append(aluno1)
        for i in range(len(duplas) - 1, posicao, -1):
            duplas[i], duplas[i - 1] = duplas[i - 1], duplas[i]

    return None


duplas = ['joel', 'juliano', 'cesar', 'auri', 'zito']
assert insere_nome('gil', duplas, 'juliano') == None
assert duplas == ['joel', 'gil', 'juliano', 'cesar', 'auri', 'zito']
assert insere_nome('marta', duplas, 'vera') == None
assert duplas == ['joel', 'gil', 'juliano', 'cesar', 'auri', 'zito', 'marta']
assert insere_nome('raffael', duplas, 'joel') == None
assert duplas == ['raffael', 'joel', 'gil', 'juliano', 'cesar', 'auri', 'zito', 'marta']
assert insere_nome('mateus', duplas, 'livia') == None
assert duplas == ['raffael', 'joel', 'gil', 'juliano', 'cesar', 'auri', 'zito', 'marta', 'mateus']
assert insere_nome('livia', duplas, 'mateus') == None
assert duplas == ['raffael', 'joel', 'gil', 'juliano', 'cesar', 'auri', 'zito', 'marta', 'livia','mateus']