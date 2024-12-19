def tem_afinidade(l1, l2):
    controle = 0

    if len(l1) > len(l2):
        maior = len(l1)
        menor = len(l2)
        lista_maior = l1
        lista_menor = l2
    else:
        maior = len(l2)
        menor = len(l1)
        lista_maior = l2
        lista_menor = l1

    for i in range(menor):
        for ii in range(maior):
            if lista_menor[i] == lista_maior[ii]:
                controle += 1
                if controle >= 3:
                    return True
    
    return False


l2 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
l1 = ['zeze', 'joao', 'oi', 'jquest']
assert tem_afinidade(l2, l1) == False

l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
l2 = ['zeze', 'joao', 'u2', 'jquest']
assert tem_afinidade(l1, l2) == True

lista_raffael = ["lady gaga", "foals", "provinz", "hello"]
lista_mateus = ["lady gaga", "foals", "miley"]
assert  tem_afinidade(lista_raffael, lista_mateus) == False
