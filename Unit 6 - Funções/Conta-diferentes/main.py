def conta_diferentes(s1, s2):
    if len(s1) > len(s2):
        menor = len(s2)
    elif len(s1) < len(s2):
        menor = len(s1)
    else:
        menor = len(s1)

    diferentes = 0

    for i in range(menor):
        if s1[i] != s2[i]:
            diferentes += 1
    return diferentes


assert conta_diferentes('aaa', 'bbb') == 3
assert conta_diferentes('oi', 'ola') == 1
assert conta_diferentes('ola', 'oi') == 1
assert conta_diferentes('nome123', 'nome') == 0
assert conta_diferentes('senha', 'Senha') == 1
