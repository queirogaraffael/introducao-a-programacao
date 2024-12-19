def dentro(numero, lista):
    for i in range(len(lista)):
        if numero == lista[i]:
            return True
    return False


def filtra_alunos(alunos, inscritos, media):
    removidos = 0

    for i in range(len(alunos) - 1, -1, -1):
        if alunos[i][1] < media or not dentro(alunos[i][0], inscritos):
            removidos += 1
            alunos.pop(i)

    return removidos



inscritos = [121, 123, 124]
alunos = [(120, 8.0), (121, 7.5), (122, 5.0), (123, 6.0), (124, 9.0),
          (125, 4.0)]
assert filtra_alunos(alunos, inscritos, 7.0) == 4
assert alunos == [(121, 7.5), (124, 9.0)]

inscritos2 = [120, 121, 122, 123, 124, 125]
aluno2 = [(120, 8.0), (121, 7.5), (122, 7.0), (123, 7.0), (124, 9.0),
          (125, 7.0)]
assert filtra_alunos(aluno2, inscritos2, 7.0) == 0
assert aluno2 == [(120, 8.0), (121, 7.5), (122, 7.0), (123, 7.0), (124, 9.0),
                  (125, 7.0)]

inscritos3 = [121, 123, 124]
alunos3 = [(120, 6.9), (121, 6.9), (122, 6.9), (123, 6.0), (124, 6.0),
           (125, 7.1)]

assert filtra_alunos(alunos3, inscritos3, 7.0) == 6
assert alunos3 == []
