posicao = 1

while True:
    nome = list(input())
    vogal, consoante = 0, 0

    for i in range(len(nome)):
        if nome[i] in "AaEeIiOoUu":
            vogal += 1
        else:
            consoante += 1

    if consoante > vogal: break
    posicao+=1

print(posicao)

"""

Mouse
casa
exemplo
Outra
lapis

3"""
