nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
n_faltas = float(input())

media = (nota1+nota2+nota3)/3
frenquencia = 1 - (n_faltas/30)

if frenquencia<0.75:
  print(f"reprovado por faltas")
elif media<4:
  print(f"reprovado por nota")
elif frenquencia>=0.75 and 4<=media<7:
  print(f"prova final")
else:
  print(f"aprovado por media")