def subtracao(m1,m2):
  matriz = []

  for i in range(len(m2)):
      apoio = []
      for j in range(len(m2[0])):
        apoio.append(m2[i][j])
      matriz.append(apoio)

  for i in range(len(matriz)):
      for j in range(len(matriz[0])):
          matriz[i][j] -= m1[i][j]

  return matriz


def soma(m1,m2):
  matriz = []
  for i in range(len(m1)):
      apoio = []
      for j in range(len(m1[0])):
          soma = m1[i][j] + m1[i][j]
          apoio.append(soma)
      matriz.append(apoio)
  return matriz


def constante(m1,m2,k):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] += k
            m2[i][j] += k
      

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

