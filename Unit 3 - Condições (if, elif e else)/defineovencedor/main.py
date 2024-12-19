nome1 = input()
nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

nome2 = input()
nota4 = int(input())
nota5 = int(input())
nota6 = int(input())


def maior(argumento1, argumento2, argumento3):
    maior = argumento1

    if argumento2 > maior:
        maior = argumento2
    if argumento3 > maior:
        maior = argumento3

    return maior


def menor(argumento1, argumento2, argumento3):
    menor = argumento1

    if argumento2 < menor:
        menor = argumento2
    if argumento3 < menor:
        menor = argumento3

    return menor


maior1 = maior(nota1, nota2, nota3)
maior2 = maior(nota4, nota5, nota6)

menor1 = menor(nota1, nota2, nota3)
menor2 = menor(nota4, nota5, nota6)

media1 = (maior1 + menor1) / 2
media2 = (maior2 + menor2) / 2

if media1 > media2:
    print(f"{nome1} venceu com nota {media1:.1f}.")
elif media2 > media1:
    print(f"{nome2} venceu com nota {media2:.1f}.")
elif media1 == media2:
    if maior1 > maior2:
        print(
            f"{nome1} venceu (no critério de desempate) com nota {media1:.1f}."
        )
    elif maior2 > maior1:
        print(
            f"{nome2} venceu (no critério de desempate) com nota {media2:.1f}."
        )
    else:
        print(f"{nome1} e {nome2} venceram com nota {media1:.1f}.")
