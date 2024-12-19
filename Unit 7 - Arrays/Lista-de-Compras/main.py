def adiciona_item(item, lista):
    lista.append(item)

    for i in range(len(lista) - 1, 0, -1):
        if lista[i] < lista[i - 1]:
            lista[i], lista[i - 1] = lista[i - 1], lista[i]


lista = ['acucar', 'leite', 'paes', 'queijo']
adiciona_item('cafe', lista)
assert lista == ['acucar', 'cafe', 'leite', 'paes', 'queijo']

lista = ['acucar', 'cafe', 'leite', 'paes']
adiciona_item('queijo', lista)
assert lista == ['acucar', 'cafe', 'leite', 'paes', 'queijo']

lista = ['cafe', 'leite', 'paes', 'queijo']
adiciona_item('acucar', lista)
assert lista == ['acucar', 'cafe', 'leite', 'paes', 'queijo']

lista = ['cafe', 'leite', 'paes']
adiciona_item('acucar', lista)
assert lista == ['acucar', 'cafe', 'leite', 'paes']