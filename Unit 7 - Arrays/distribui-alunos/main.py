def distribui_alunos(t1, t2, capacidade):
  resultado = [[],[]]

  if len(t1)>len(t2):
    maior = len(t1)
  else:
    maior = len(t2)

  controle = 0
  valor = 0

  for i in range(maior):
    if i < len(t1):
      resultado[valor].append(t1[i])
      controle+=1

    if controle >= capacidade:
      valor = 1

    if i < len(t2):
      resultado[valor].append(t2[i])
      controle+=1

    if controle >= capacidade:
      valor = 1

  return resultado


t1 = [10, 38, 87, 22, 25]
t2 = [43, 21, 96, 33, 85, 17, 94]
assert distribui_alunos(t1, t2, 6) == [[10, 43, 38, 21, 87, 96], [22, 33, 25, 85, 17, 94]]


t1 = [10, 38, 87, 22, 25]
t2 = [43]
assert distribui_alunos(t1, t2, 5) == [[10, 43, 38, 87, 22], [25]]


t1 = [10, 38, 87, 22, 25]
t2 = [43, 21, 96, 33, 85]
assert distribui_alunos(t1, t2, 5) == [[10, 43, 38, 21, 87], [96, 22, 33, 25, 85]]