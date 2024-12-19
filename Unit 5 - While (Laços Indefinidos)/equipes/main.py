#prog1
# UFCG - computação
# Raffael queiroga
# Data: 06/10/2021
# prova 3
# O programa lê o nome de diversos atletas e informa qual a # modalidade de competição

num_jogadores = 0

while True:
    nome = input()
    if nome == "-": break
    num_jogadores += 1

if num_jogadores == 5:
    print("Modalidade -> Basquete")
elif num_jogadores == 6:
    print("Modalidade -> Vôlei")
elif num_jogadores == 7:
    print("Modalidade -> Handebol")
elif num_jogadores == 11:
    print("Modalidade -> Futebol")
else:
    print("Equipe Inválida")
