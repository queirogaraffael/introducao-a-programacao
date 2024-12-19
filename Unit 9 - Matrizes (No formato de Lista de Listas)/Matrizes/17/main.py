def menor(a, b, c):
    menor = a
    controle = 1

    if b < menor:
        menor = b
        controle = 2

    if c < menor:
        controle = 3

    return controle


def pior_nota(m):
    pior_nota_1, pior_nota_2, pior_nota_3 = [], [], []

    for i in range(len(m)):
        controle = menor(m[i][0], m[i][1], m[i][2])
        aluno = "Aluno " + str(i + 1)

        if controle == 1:
            pior_nota_1.append(aluno)
        elif controle == 2:
            pior_nota_2.append(aluno)
        else:
            pior_nota_3.append(aluno)
    
    for i in range(len(pior_nota_1)):
      print(pior_nota_1[i])
    print("---")
    for i in range(len(pior_nota_2)):
      print(pior_nota_2[i])
    print("---")
    for i in range(len(pior_nota_3)):
      print(pior_nota_3[i])
    


# 17. Leia uma matriz 10 x 3 com as notas de 10 alunos em 3 provas. Em seguida, escreva
#o número de alunos cuja pior nota foi na prova 1, o número de alunos cuja pior nota foi
#na prova 2, e o número de alunos cuja pior nota foi na prova 3. Em caso de empate
#das piores notas de um aluno, o critério de desempate é arbitrário, mas o aluno deve ser
#contabilizado apenas uma vez.


matriz = [[10,9,8],[10,8,9],[1,2,3],[6,3,4]]

pior_nota(matriz)