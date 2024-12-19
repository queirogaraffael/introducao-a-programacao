def maioridade_penal(nomes, idades):
    nomes = nomes.split()
    idades = idades.split()

    nome = ""

    for i in range(len(idades)):
        if int(idades[i]) >= 18:
            nome += nomes[i] + " "    

    if nome == "":
        return nome
    else:
        nome1 = nome.rstrip()
        return nome1


assert maioridade_penal("Jansen Italo Ana", "14 14 14") == ""

assert maioridade_penal("Jansen Italo Ana", "22 21 60") == "Jansen Italo Ana"

assert maioridade_penal("Jansen Italo Ana", "18 18 19") == "Jansen Italo Ana"
