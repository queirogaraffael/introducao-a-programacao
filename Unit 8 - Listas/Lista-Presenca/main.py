def cria_lista_presenca(turmas, nomes, turma):
    indices = []

    for i in range(len(turmas)):
        if turmas[i] == turma:
            indices.append(i)

    resultado = []

    for i in range(len(indices)):
        resultado.append(nomes[indices[i]])

    return resultado


turmas = [1, 2, 2, 4, 5, 3, 5]
nomes = ["Maria", "Pedro", "Carlos", "Ana", "Carla", "Joao", "Jose"]
assert cria_lista_presenca(turmas, nomes, 5) == ["Carla", "Jose"]
