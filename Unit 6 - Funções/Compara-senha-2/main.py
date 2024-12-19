def compara_senhas(string1, string2):

    if len(string1) > len(string2):
        menor = len(string2)
    elif len(string1) < len(string2):
        menor = len(string1)
    else:
        menor = len(string1)

    diferentes = 0

    for i in range(menor):
        if string1[i] != string2[i]:
            diferentes += 1

    return diferentes


assert compara_senhas('nome123', 'nome') == 0
assert compara_senhas('aaa', 'bbb') == 3
assert compara_senhas('senha', 'Senha') == 1
