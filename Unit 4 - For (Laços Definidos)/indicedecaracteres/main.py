string_um = list(input())
string_dois = list(input())

acumulador = []

for i in range(len(string_dois)):
    if string_dois[i] in string_um:
        for a in range(len(string_um)):
            if string_dois[i] == string_um[a]:
                acumulador.append(a)

        for indice in range(len(acumulador)):
            if len(acumulador) == 1:
                print(acumulador[indice])
            elif indice == (len(acumulador) - 1) and not indice == 0:
                print(acumulador[indice])
            else:
                print(acumulador[indice], end=" ")

        acumulador = []

    else:
        print("-1")
