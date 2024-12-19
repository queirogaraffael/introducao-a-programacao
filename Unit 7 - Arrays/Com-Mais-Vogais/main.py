def quantidade_vogal(nome):
    quantidade = 0
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(nome)):
        for j in range(len(vogais)):
            if nome[i] == vogais[j]:
                quantidade += 1
                break
    return quantidade


def maior_valor(lista):
    maior = lista[len(lista) - 1]
    for i in range(len(lista) - 1, -1, -1):
        if maior < lista[i]:
            maior = lista[i]
    return maior


def remove_palavras_com_mais_vogais(lista):
    quantidade = []
    for i in range(len(lista)):
        quantidade.append(quantidade_vogal(lista[i]))

    maior = maior_valor(quantidade)

    for i in range(len(lista) - 1, -1, -1):
        if maior != 0 and quantidade[i] == maior :
            lista.pop(i)

    return None


lista1 = ['arara', 'tv', 'bacia']
assert remove_palavras_com_mais_vogais(lista1) == None
assert lista1 == ['tv']

lista1 = ['mtv', 'tv', 'tvz']
assert remove_palavras_com_mais_vogais(lista1) == None
assert lista1 == ['mtv', 'tv', 'tvz']

lista1 = ['mtva', 'tva', 'tva']
assert remove_palavras_com_mais_vogais(lista1) == None
assert lista1 == []

lista1 = ['mtv', 'tv', 'tva']
assert remove_palavras_com_mais_vogais(lista1) == None
assert lista1 == ['mtv', 'tv']

lista1 = ['arara', 'tv', 'baci']
assert remove_palavras_com_mais_vogais(lista1) == None
assert lista1 == ['tv', 'baci']

lista1 = ['mtv', 'tva', 'tvaA']
assert remove_palavras_com_mais_vogais(lista1) == None
assert lista1 == ['mtv', 'tva']
