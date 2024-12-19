def z_inicial(lista):
    controle = 0
    for i in range(len(lista)):
        if lista[i][0] == "z" or lista[i][0] == "Z":
            controle += 1
    return controle


lista1 = ["zumbi", "Zeca", "Recife"]
lista2 = ["livro", "cd", "software"]
assert z_inicial(lista1) == 2
assert z_inicial(lista2) == 0

nomes = input().split()
print(z_inicial(nomes))
"""
zumbi Zeca Recife
2
"""
