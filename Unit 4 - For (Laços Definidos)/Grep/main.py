palavra = list(input())
N = int(input())


for i in range(N):
    nome = list(input())
    for i in range(len(nome)):
        if i<=len(nome)-3:
            if palavra[0] == nome[i]:
                if palavra[1] == nome[i + 1]:
                    if palavra[2] == nome[i + 2]:
                      ok = "".join(nome)
                      print(ok)


"""
python grep.py
ola
3
um exemplo de frase
outro ola frase
outro ola frase
frase"""