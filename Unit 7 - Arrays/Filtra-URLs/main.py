def dentro(nome):
    google = ['g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm']
    for i in range(len(nome) - len(google) + 1):
        controle = i
        controle2 = 0
        for j in range(len(google)):
            if nome[controle] == google[j]:
                controle2 += 1
                controle += 1
                if controle2 == len(google):
                    return True
    return False


def filtra_urls(l):
    nova_lista = []

    for i in range(len(l)):
        nova_lista.append(l[i])

    for i in range(len(nova_lista) - 1, -1, -1):
        if not dentro(nova_lista[i]):
            nova_lista.pop(i)

    return nova_lista


p1 = ['www.uol.com', 'www.google.com', 'http://mail.google.com']
assert filtra_urls(p1) == ['www.google.com', 'http://mail.google.com']

p1 = ['www.uol.com', 'www.googlle.com', 'http://mail.google.com']
assert filtra_urls(p1) == ['http://mail.google.com']

p1 = ['www.uol.com', 'google.com', 'http://mail.google.com']
assert filtra_urls(p1) == ['google.com', 'http://mail.google.com']

p1 = ['www.uol', 'www.google.com', 'http://mail.google.com']
assert filtra_urls(p1) == ['www.google.com', 'http://mail.google.com']

p1 = ['www.uol.com', 'www.google.com', 'google.comhttp://mail.']
assert filtra_urls(p1) == ['www.google.com', 'google.comhttp://mail.']

p1 = ['www.uol.com', 'www.google.com', 'oogle.comhttp://mail.', 'google.cohttp://mail.']
assert filtra_urls(p1) == ['www.google.com']

p1 = ['www.uol.com', 'www.googlle.com', 'http://mail.oogle.com']
assert filtra_urls(p1) == []
assert p1 == ['www.uol.com', 'www.googlle.com', 'http://mail.oogle.com']