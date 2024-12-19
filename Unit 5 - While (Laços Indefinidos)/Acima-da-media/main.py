valor_medio_mensal = float(input())

guarda = []
controle = 0


def media(sequencia):
    lista1 = sequencia.split()
    soma, divisor = 0, 0
    for i in range(len(lista1)):
        soma += int(lista1[i])
        divisor += 1
    media = soma / divisor
    return media


while True:
    sequencia = input()
    if sequencia == "fim": break
    if media(sequencia) < valor_medio_mensal / 2: break

    if media(sequencia) > valor_medio_mensal:
        guarda.append(sequencia)
        controle += 1

if guarda != []:
    for i in range(len(guarda)):
        print(guarda[i])


"""
100.0
77 72 65
101 110
fim
101 110

$ python joao.py
20.0
120 110 12
9 8
120 110 12"""
