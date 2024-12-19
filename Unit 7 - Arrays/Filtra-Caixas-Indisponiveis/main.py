def filtra_caixas_indisponiveis(lista_caixas, qtd_itens):
    for i in range(len(lista_caixas) - 1, -1, -1):
        if lista_caixas[i] < qtd_itens:
            lista_caixas.pop(i)


caixas = [0, 1, 2, 3, 4, 5, 6]
filtra_caixas_indisponiveis(caixas, 3)
assert caixas == [3, 4, 5, 6]

caixas = [0, 1, 2, 3, 4, 5, 6]
filtra_caixas_indisponiveis(caixas, 0)
assert caixas == [0, 1, 2, 3, 4, 5, 6]
