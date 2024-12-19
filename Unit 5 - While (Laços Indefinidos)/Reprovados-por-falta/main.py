reprovados = 0

while True:
  entrada = list(input())
  if entrada[0] == "-" :break

  contador = 0

  for i in range(len(entrada)):
    if "f" == entrada[i]:
      contador+=1

  if contador>8:
    reprovados+=1


print(f"{reprovados} aluno(s) reprovado(s) por falta.")

"""
python joao.py
... ... f.. ...f.
fff fff fff fffff
... ... f.. ...f.
..f fff fff f..f.
-
2 aluno(s) reprovado(s) por falta."""
