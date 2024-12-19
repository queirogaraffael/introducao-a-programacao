def matriz(matriz,gabarito):
    resultado = []

    for i in range(len(matriz)):
        acertos = 0
        for j in range(len(matriz[0])):
          if matriz[i][j] == gabarito[j]:
              acertos += 1
        resultado.append(acertos)
    
    for i in range(len(resultado)):
      print(f"Aluno {i + 1}: {resultado[i]} acertos")


gabarito = ["a","d","b","a","c","b","a","c","d","b"]
resultado = [["a","d","b","a","c","b","a","c","d","b"],["a","d","b","a","c","b","a","c","d","a"],["b","a","b","a","c","b","a","c","d","b"],["d","a","a","a","c","b","a","c","d","b"],["b","b","a","b","c","b","a","c","d","b"]]

matriz(resultado,gabarito)




#15. Leia uma matriz 5 x 10 que se refere respostas de 10 questões de múltipla escolha,
#referentes a 5 alunos. Leia também um vetor de 10 posições contendo o gabarito de
#respostas que podem ser a, b, c ou d. Seu programa deverá comparar as respostas
#de cada candidato com o gabarito e emitir um vetor denominado resultado, contendo a
#pontuação correspondente a cada aluno.