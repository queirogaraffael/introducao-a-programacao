def funcao_GE(lista):
    for i in range(len(lista) - 1, 0, -1):
        lista[i], lista[i - 1] = lista[i - 1], lista[i]
    string = " ".join(lista)
    string = string.rstrip()
    return string


def funcao_GD(lista):
    for i in range(len(lista) - 1):
        lista[i], lista[i + 1] = lista[i + 1], lista[i]
    string = " ".join(lista)
    string = string.rstrip()
    return string


def funcao_I(lista):
    for i in range(len(lista) - 1):
        if i % 2 == 0:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
    string = " ".join(lista)
    string = string.rstrip()
    return string


valores, operacoes = [], []

valores = list(input().split())

while True:
    operacao = input()
    if operacao == "fim": break
    operacoes.append(operacao)

for i in range(len(operacoes)):
    if operacoes[i] == 'GE':
        print(funcao_GE(valores))
    elif operacoes[i] == 'GD':
        print(funcao_GD(valores))
    else:
        print(funcao_I(valores))
"""
A 2 3 4 5
I
fim
2 A 4 3 5


- input: |
    A 2 3 4 5
    I
    fim
  output: |
    2 A 4 3 5

- input: |
    K 2 7
    GD
    GD
    GE
    fim
  output: |
    2 7 K
    7 K 2
    2 7 K

- input: |
    A 2 3 4 5
    I
    GE
    GD
    fim
  output: |
    2 A 4 3 5
    5 2 A 4 3
    2 A 4 3 5

- input: |
    K 2 7
    GE
    GE
    GD
    I
    fim
  output: |
    7 K 2
    2 7 K
    7 K 2
    K 7 2

- input: |
    K 2
    GD
    GE
    I
    fim
  output: |
    2 K
    K 2
    2 K

- input: |
    K 2
    I
    fim
  output: |
    2 K
"""
